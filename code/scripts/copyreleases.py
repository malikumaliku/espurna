from __future__ import print_function

#https://docs.platformio.org/en/latest/projectconf/advanced_scripting.html

Import("env", "projenv")

from shutil import copyfile
import os

#print(env.Dump())
#print(projenv.Dump())

releasesdir = os.path.join(env.subst("$PROJECT_DIR"), "releases")
os.makedirs(releasesdir, exist_ok=True)

origfile = os.path.join(env.subst("$BUILD_DIR"),env.subst("$PROGNAME")+".bin")
envflags = env.ParseFlags(env['BUILD_FLAGS'])
cppdefines = envflags.get("CPPDEFINES")
defines = {}
for entry in cppdefines:
    if isinstance(entry, str):
        defines[entry] = ""
    elif isinstance(entry, list):
        defines[entry[0]] = entry[1]
#print(defines)
version = defines.get("APP_VERSION")
if version[0]=="\"" and version [len(version)-1]=="\"":
    version = version[1:-1]
#print(version)
destfile = os.path.join(releasesdir,env.subst("$PIOENV")+"+"+version+".bin")

print("copy file from",origfile,"into",destfile)

if os.path.isfile(destfile):
    os.remove(destfile) 
if os.path.isfile(origfile):
    copyfile(origfile,destfile)
