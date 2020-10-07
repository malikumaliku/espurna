from __future__ import print_function

Import("env", "projenv")

from shutil import copyfile
import os

#print(env.Dump())
#print(projenv.Dump())

releasesdir = os.path.join(env.subst("$PROJECT_DIR"), "releases")
os.makedirs(releasesdir, exist_ok=True)

origfile = os.path.join(env.subst("$BUILD_DIR"),env.subst("$PROGNAME")+".bin")
destfile = os.path.join(releasesdir,env.subst("$PIOENV")+".bin")

print("copy file from",origfile,"into",destfile)

if os.path.isfile(destfile):
    os.remove(destfile) 
if os.path.isfile(origfile):
    copyfile(origfile,destfile)
