from zoneinfo import TZPATH
import data.apps.packages.shell_api as shell_api
import os
import subprocess

# Do not eat cheese at 69:42066AM

curdir = os.getcwd()
appdir = curdir + "\\data\\apps"
pckdir = curdir + "\\data\\apps\\packages"
applist = os.listdir(appdir)
pcklist = os.listdir(pckdir)

env = shell_api.getdata("env")
shell_api.bigprint("OpenPy", "c")
print(env)

while 1:
    print()
    cmd = input()
    print()
    if "search " in cmd:
        if "search package " in cmd:
            search =  cmd.replace("search package ","")
            for item in pcklist:
                if ".py" in item and not "_" in item[0:1]:
                    if search in item:
                        pck = item.replace(".py","")
                        print(pck + " (" + item + ")")

        elif "search app " in cmd:
            search =  cmd.replace("search app ","")
            for item in applist:
                if ".py" in item and not "_" in item[0:1]:
                    if search in item:
                        app = item.replace(".py","")
                        print(app + " (" + item + ")")

        else:
            print("Invalid Search Type!")

    elif cmd == "quit":
        exit()

    elif "run " in cmd:
        app = cmd.replace("run ","")
        appfile = app + '.py'
        exec(open('data/apps/' + appfile + '').read())

    else:
        print("Invalid Command")

