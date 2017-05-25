import sys
import os
import platform
import time
import ctypes
import csv
import threading
from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)

from array import *
from ctypes import *
from __builtin__ import exit

if sys.platform.startswith('win32'):
    import msvcrt
elif sys.platform.startswith('linux'):
    import atexit
    from select import select

from ctypes import *

try:
    if sys.platform.startswith('win32'):
        libEDK = cdll.LoadLibrary("/bin/win32/edk.dll")
    elif sys.platform.startswith('linux'):
        srcDir = os.getcwd()
	if platform.machine().startswith('arm'):
            libPath = srcDir + "/bin/armhf/libedk.so"
	else:
            libPath = srcDir + "/bin/linux64/libedk.so"
        libEDK = CDLL(libPath)
    else:
        raise Exception('System not supported.')
except Exception as e:
    print 'Error: cannot load EDK lib:', e
    exit()

class DataCollector(QThread):

    IEE_EmoEngineEventCreate = libEDK.IEE_EmoEngineEventCreate
    IEE_EmoEngineEventCreate.restype = c_void_p
    eEvent = IEE_EmoEngineEventCreate()

    IEE_EmoEngineEventGetEmoState = libEDK.IEE_EmoEngineEventGetEmoState
    IEE_EmoEngineEventGetEmoState.argtypes = [c_void_p, c_void_p]
    IEE_EmoEngineEventGetEmoState.restype = c_int

    IEE_EmoStateCreate = libEDK.IEE_EmoStateCreate
    IEE_EmoStateCreate.restype = c_void_p
    eState = IEE_EmoStateCreate()

    userID = c_uint(0)
    user   = pointer(userID)
    ready  = 0
    state  = c_int(0)

    alphaValue     = c_double(0)
    low_betaValue  = c_double(0)
    high_betaValue = c_double(0)
    gammaValue     = c_double(0)
    thetaValue     = c_double(0)

    alpha     = pointer(alphaValue)
    low_beta  = pointer(low_betaValue)
    high_beta = pointer(high_betaValue)
    gamma     = pointer(gammaValue)
    theta     = pointer(thetaValue)

    shared = False

    def run(self):
        self.startCollect()
    
    def setName(self,name):
        self.file = open('./output/'+ name +'.csv','wb')

    # stop process
    def stop(self):
        self.shared = True

    # set file name for the data recording file
    def startCollect(self):
        writer = csv.writer(self.file)
        channelList = array('I',[3, 7, 9, 12, 16])   # IED_AF3, IED_AF4, IED_T7, IED_T8, IED_Pz 
        dataTypes = ["Time, Theta", "Alpha", "Low_beta", "High_beta", "Gamma"]
        # -------------------------------------------------------------------------
        print "==================================================================="
        print "Example to get the average band power for a specific channel from" \
        " the latest epoch."
        print "==================================================================="

        # -------------------------------------------------------------------------
        if libEDK.IEE_EngineConnect("Emotiv Systems-5") != 0:
                print "Emotiv Engine start up failed."
                exit()

        # headlist writing
        headList = []
        for i in channelList:
            for j in dataTypes:
                headList.append(str(i) + " " + str(j))

        print "Time, Theta, Alpha, Low_beta, High_beta, Gamma \n"
        writer.writerow(headList)
        # headlist writing is over
        # start = time.time()
        
        while (1):
            if self.shared == True:
                print "break"
                break
            
            state = libEDK.IEE_EngineGetNextEvent(self.eEvent)
            
            if state == 0:
                eventType = libEDK.IEE_EmoEngineEventGetType(self.eEvent)
                libEDK.IEE_EmoEngineEventGetUserId(self.eEvent, self.user)
                if eventType == 16:  # libEDK.IEE_Event_enum.IEE_UserAdded
                    ready = 1
                    libEDK.IEE_FFTSetWindowingType(self.userID, 1);  # 1: libEDK.IEE_WindowingTypes_enum.IEE_HAMMING
                    print "User added"
                
                                
                if ready == 1:
                    # end = time.time()
                    # time = (end - start)
                    listData = []
                    # listData.append(time)
                    for i in channelList: 
                        result = c_int(0)
                        result = libEDK.IEE_GetAverageBandPowers(self.userID, i, self.theta, self.alpha, self.low_beta, self.high_beta, self.gamma)
                        
                        if result == 0:    #EDK_OK
                            print i
                            print "%.6f, %.6f, %.6f, %.6f, %.6f" % (self.thetaValue.value, self.alphaValue.value, 
                                                                    self.low_betaValue.value, self.high_betaValue.value, self.gammaValue.value)

                            # writer.writerow(thetaValue.value, alphaValue.value,low_betaValue.value, high_betaValue.value, gammaValue.value)
                            listData.extend((self.thetaValue.value, self.alphaValue.value, self.low_betaValue.value, self.high_betaValue.value, self.gammaValue.value))
                    print "\n"
                    writer.writerow(listData)    
            elif state != 0x0600:
                print "Internal error in Emotiv Engine ! "
            time.sleep(0.1)
        # -------------------------------------------------------------------------
        self.file.close()
        libEDK.IEE_EngineDisconnect()
        libEDK.IEE_EmoStateFree(self.eState)
        libEDK.IEE_EmoEngineEventFree(self.eEvent)
