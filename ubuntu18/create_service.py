import sys
import os
import re

def writeLn(f,s):
    f.write("{}\n".format(s))

def make_service(path,dname,shname):
    fname = "usr_{}.service".format(dname)
    dpath = os.path.join(path,dname)
    fpath = os.path.join(dpath,fname)
    with open(fpath,"w") as f:
        c = get_service_contents(dpath,shname)
        for l in c:
            writeLn(f,l)

def get_service_contents(dpath,fn):
    return [ "[Unit]"
           , "Description=activate user-program sample"
           , ""
           , "[Service]"
           , "Type=simple"
           , "ExecStart={}".format(os.path.join(dpath,fn))
           # , "Restart=always"
           , "Restart=no"
           , ""
           , "[Install]"
           , "WantedBy=multi-user.target"
           ]

def make_shell(path,dname,shname):
    fname = shname
    dpath = os.path.join(path,dname)
    fpath = os.path.join(dpath,fname)
    with open(fpath,"w") as f:
        c = get_shell_contents(dpath,shname)
        for l in c:
            writeLn(f,l)

def get_shell_contents(dpath,fn):
    return [ "#!/bin/bash"
           , "TGT={}".format(dpath)
           , "python $TGT/{}.py $TGT".format(fn)
           , ""
           ]


def main(args):
    if(3<len(args)):
        make_service(args[1],args[2],args[3])
    else:
        print("error: less args.")

if(__name__=="__main__"):
    main(sys.argv)

