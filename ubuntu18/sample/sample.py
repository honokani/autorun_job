import sys
import os
import re
import datetime
import time

def getCurrFilePath():
    return os.path.realpath(__file__)

def getCurrDirPath():
    return os.path.dirname(getCurrFilePath())

def getContetsNames(fPath=getCurrDirPath()):
    files = []
    dirs = []
    for tgt in os.listdir(fPath):
        if (os.path.isfile(os.path.join(fPath,tgt))):
            files.append(tgt)
        else:
            dirs.append(tgt)
    return dirs, files


def findDirByFullname(fPath=getCurrDirPath(), fullname=""):
    dirs, _ = getContetsNames(fPath)
    if (fullname==""):
        return dirs
    else:
        founds = []
        fullname = fullname.lower()
        tgt = re.compile("^{}$".format(fullname))
        for d in dirs:
            if (not None==tgt.search(d.lower())):
                founds.append(d)
        return founds



def write_log_forever(path):
    dname = "active_check"
    fname = "log.txt"
    ds = findDirByFullname(path,dname)
    if(0<len(ds)):
        ac_n = ds[0]
        ac_p = os.path.join(path,ac_n)
        with open(os.path.join(ac_p,fname),"a") as f:
            for i in range(60):
                dt = datetime.date.today()
                tm = datetime.datetime.now()
                f.write("{} {} {}\n".format(i, dt,tm))
                time.sleep(10)
    else:
        print("error: dirs not found")

def main(args):
    if(1<len(args)):
        write_log_forever(args[1])
    else:
        print("error: less args.")

if(__name__=="__main__"):
    main(sys.argv)

