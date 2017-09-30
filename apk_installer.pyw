import sys
import os
import time
import shlex,subprocess

try:
    apk_name = sys.argv[1]
    #print apk_name

    #os.system('adb install -r ' + apk_name) #will spawn command prompt,so 
    
    cmd = 'adb install -r ' + apk_name
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = subprocess.SW_HIDE
    #si.wShowWindow = subprocess.SW_HIDE # hide command prompt window

    # p = subprocess.Popen(shlex.split(cmd),shell=True)
    
    p = subprocess.Popen(cmd,startupinfo = si,shell = True)
    p.wait() #waitting for child process to terminate
    # DETACHED_PROCESS = 0x00000008
    # subprocess.call(cmd, creationflags = DETACHED_PROCESS)
    
except:
    pass
    