import data.apps.apppck.shell_api as shell_api
import os
import platform

# Do not eat cheese at 69:42066AM

curdir = os.getcwd()

if not platform.system() == "Windows":
    appdir = curdir + "/data/apps"
    gamedir = curdir + "/data/games"
    apppckdir = curdir + "/data/apps/apppck"
    gamepckdir = curdir + "/data/apps/gamepck"
else:
    appdir = curdir + "\\data\\apps"
    gamedir = curdir + "\\data\\games"
    apppckdir = curdir + "\\data\\apps\\apppck"
    gamepckdir = curdir + "\\data\\apps\\gamepck"
applist = os.listdir(appdir)
apppcklist = os.listdir(apppckdir)
gamelist = os.listdir(gamedir)
gamepcklist = os.listdir(gamepckdir)

env = shell_api.getdata("env")
shell_api.bigprint("OpenPy", "c")
print(env)

while 1:
    print()
    cmd = input("open_py> ") 
    print()
    if "search " in cmd:
        if "search app package " in cmd:
            search =  cmd.replace("search apppck ","")
            print("----------------------------------------")
            print("Results:")
            for item in apppcklist:
                if ".py" in item and not "_" in item[0:1]:
                    if search in item:
                        apppck = item.replace(".py","")
                        print(apppck + " (" + item + ")")
            print("----------------------------------------")

        elif "search app " in cmd:
            search =  cmd.replace("search app ","")
            print("----------------------------------------")
            print("Results:")
            for item in applist:
                if ".py" in item and not "_" in item[0:1]:
                    if search in item:
                        app = item.replace(".py","")
                        print(app + " (" + item + ")")
            print("----------------------------------------")

        elif "search game package " in cmd:
            search =  cmd.replace("search game package ","")
            print("----------------------------------------")
            print("Results:")
            for item in gamepcklist:
                if ".py" in item and not "_" in item[0:1]:
                    if search in item:
                        gamepck = item.replace(".py","")
                        print(gamepck + " (" + item + ")")
            print("----------------------------------------")

        elif "search game " in cmd:
            search =  cmd.replace("search game ","")
            print("----------------------------------------")
            print("Results:")
            for item in gamelist:
                if ".py" in item and not "_" in item[0:1]:
                    if search in item:
                        game = item.replace(".py","")
                        print(game + " (" + item + ")")
            print("----------------------------------------")

        else:
            print("Invalid Search Type!")

    elif cmd == "quit":
        exit()

    elif "run " in cmd:
        app = cmd.replace("run ","")
        appfile = app + '.py'
        exec(open('data/apps/' + appfile + '').read())

    elif cmd == "clear":
        shell_api.clear()

    else:
        print("Invalid Command")

