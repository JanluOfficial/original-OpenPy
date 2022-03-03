import os
import platform

# Basic Commands

def bigprint(text, alignment):
    charnum = len(text)
    if charnum > 38: print("Warning: Amount of characters too high!")
    else:
        if alignment == "left" or alignment == "l":
            print("########################################")
            print(" " + text + "")
            print("########################################")
        elif alignment == "center" or alignment == "c":
            charnum = round(charnum)
            calc1 = int(40) / int(2)
            calc2 = int(charnum) / 2
            calc = int(calc1) - int(calc2)
            spaces = "                                        "
            beforetext = spaces[0:calc]
            print("########################################")
            print("" + beforetext + "" + text + "")
            print("########################################")
        elif alignment == "right" or alignment == "r":
            spaces = "                                        "
            spacestokeep = int(len(spaces)) - int(charnum)
            beforetext = spaces[0:spacestokeep]
            print("########################################")
            print("" + beforetext + "" + text + "")
            print("########################################")

def getdata(data):
    if data == "env":
        osname = platform.system()
        if osname == "Darwin":
            osname = "Mac OS"
        osrelease = platform.release()
        osarchitecture = platform.architecture()
        osbuild = platform.version()
        returndata = osname + ' ' + str(osrelease) + ' ' + str(osbuild) + str(osarchitecture)

    elif data == "env_list":
        osname = platform.system()
        if osname == "Darwin":
            osname = "Mac OS"
        osrelease = platform.release()
        osarchitecture = platform.architecture()
        osbuild = platform.version()

        returndata = [osname, osrelease, osbuild, osarchitecture]

    elif data == "consize":
        terminalsize = os.get_terminal_size()
        returndata = terminalsize.replace("os.","")

    elif data == "pyver":
        pyver = platform.python_version()

        returndata = pyver
        return returndata

    else:
        returndata = 'Invalid Data Type!'
    return returndata

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def newfunc():
    print("Comming Soon!")