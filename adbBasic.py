#!/usr/bin/python3

from os.path import getsize, split
import subprocess
import os
import time
import sys
import datetime


helpMenu = """
Options :
    
   - home        : Home Button
   - back        : Back Button
   - right       : Right Button
   - left        : Left button
   - up          : Up Button
   - down        : Down Button
   - volume up   : Volume Up Button
   - volume down : Volume Down Button
   - enter       : OK Button
   - text    ... : Send Text
   - listapp     : List Installed App Packages Name
   - listallapp  : List All App Packages Name 
   - install ... : Install App
   - uninstall   : Uninstall App
   - runapp  ... : Start App With Package Name
   - stopapp     : Stop App With Package Name
   - wakeup      : Wake Up Device
   - sleep       : Sleep Mode
   - shutdown    : Shutdown Device ( if you turn off the device the connection is gone)
   - screencap   : Take a Screenshot
   - screenrec   : Screen Recorder
   - livescreen  : Live Screen Viewer
   - clearapp    : Clear App Cache and Data With Package Name
   - browser     : Open Browser
   - takepic     : Take Camera Picture (in the camera application needs in)
   - resume      : Resume Playing
   - pause       : Pause Playing
   - mute        : Mute
   - assistant   : Open the voice assistant
   - getmodel    : Show Device Model
   - getbattery  : Show Device Battery
   - getsize     : Show Screen Resolution
   - getid       : Shot android_id
   - getversion  : Show Android Version
   - ifconfig    : Show IP Address
   - ps          : See Process
   - top         : View real-time resource consumption 
   - getmac      : Show MAC Address
   - cpuinfo     : Show CPU Information
   - meminfo     : Show Memory Information
   - pull        : Get File to Device  | <android-path> <computer-path>
   - push        : Send File to Device | <computer-path> <android-path>
"""


##Functions##

def home():

    os.system("adb shell input keyevent KEYCODE_HOME")


def back():

    os.system("adb shell input keyevent KEYCODE_BACK")


def volume_up():

    os.system("adb shell input keyevent KEYCODE_VOLUME_UP")


def volume_down():

    os.system("adb shell input keyevent KEYCODE_VOLUME_DOWN")


def enter():

    os.system("adb shell input keyevent KEYCODE_ENTER")


def text(text):

    os.system("adb shell input text " + str(text[4::]))


def list_app():

    adbListPackages = subprocess.check_output("adb shell pm list packages -3", shell=True).decode("utf-8")

    splitLine = adbListPackages.splitlines()

    return splitLine


def list_all_app():

    adbListPackages = subprocess.check_output("adb shell pm list packages ", shell=True).decode("utf-8")

    splitLine = adbListPackages.splitlines()

    return splitLine


def clear():

    os.system(clear)


def install(user_input):

    os.system("adb install " + user_input[7::])


def uninstall(user_input):

    os.system("adb uninstall " + user_input[9::])


def run_app(user_input):

    os.system("adb shell monkey -p {0} -c android.intent.category.LAUNCHER 1".format(user_input[6::]))


def stop_app(user_input):

    os.system("adb shell am force-stop {}".format(user_input[7::]))


def wake_up():

    os.system("adb shell input keyevent KEYCODE_WAKEUP")

    time.sleep(1)


def sleep():

    os.system("adb shell input keyevent 6")


def shutdown():

    os.system("adb shell reboot -p")

    time.sleep(1)


def right():

    os.system("adb shell input keyevent KEYCODE_DPAD_RIGHT")


def left():

    os.system("adb shell input keyevent KEYCODE_DPAD_LEFT")


def up():

    os.system("adb shell input keyevent KEYCODE_DPAD_UO")


def down():

    os.system("adb shell input keyevent KEYCODE_DPAD_DOWN")


def screenshot():

    os.system("adb exec-out screencap -p > sc.png")

    t = os.path.getatime("sc.png")

    a = datetime.datetime.fromtimestamp(t)

    timeFile = str(a).split(" ")[0] + "_" + str(a).split(" ")[1]

    filePath = os.getcwd()

    os.rename("sc.png", timeFile.split(".")[0] + ".png")

    ##download screenshot


def clear_app(user_input):

    os.system("adb shell pm clear {}".format(user_input[7::]))


def take_pic():

    os.system("adb shell input keyevent 27")


def browser():

    os.system("adb shell input keyevent 64")


def resume():

    os.system("adb shell input keyevent 126")


def pause():

    os.system("adb shell input keyevent 127")


def mute():

    os.system("adb shell input keyevent 164")


def get_model():

    os.system("adb shell getprop ro.product.model")


def get_battery():

    os.system("adb shell dumpsys battery")


def get_size():

    os.system("adb shell wm size")


def get_id():

    os.system("adb shell settings get secure android_id")


def get_version():


    os.system("adb shell getprop ro.build.version.release")


def ifconfig():

    os.system("\nadb shell ifconfig | grep Mask")


def get_mac():

    os.system("adb shell cat /sys/class/net/wlan0/address")


def cpu_info():

    os.system("adb shell cat /proc/cpuinfo")


def mem_info():

    os.system("adb shell cat /proc/meminfo")


def pull(user_input):

    splitinput = user_input.split(" ")

    if len(splitinput) != 3:

        print("Wrong Input!")
        
    else:

        os.system("adb pull {} {}".format(splitinput[1], splitinput[2]))


def push(user_input):

    splitinput1 = user_input.split(" ")

    if len(splitinput1) != 3:

        print("Wrong Input!")

    else:

        os.system("adb push {} {}".format(splitinput1[1], splitinput1[2]))


def screen_record():

    path = "/sdcard/sc.mp4" ##### change here if you want to save elsewhere #####

    os.system("adb shell screenrecord {}".format(path))


def live_screen():

    os.system("adb shell screenrecord --output-format=h264 - | ffplay -")


def assistant():

    os.system("adb shell input keyevent 231")

def main():

    try:

            userInput = input("adb> ")


            if userInput.lower() == "home":

                home()


            elif userInput.lower() == "back":
                back()


            elif userInput.lower() == "volume up":

                volume_up()


            elif userInput.lower() == "volume down":

                volume_down()


            elif userInput.lower() == "enter":

                enter()


            elif userInput[0:4] == "text":

                text(userInput)


            elif userInput.lower() == "listapp":


                print("Installed Apps :\n")

                for i in list_app():

                    print("- " + i[8::])

                print()


            elif userInput.lower() == "listallapp":


                print("All Apps :\n")

                for i in list_all_app():

                    print("- " + i[8::])

                print()


            elif userInput.lower() == "clear":

                clear()


            elif userInput.lower()[0:7] == "install":

                install(userInput)


            elif userInput.lower()[0:9] == "uninstall":

                uninstall(userInput)


            elif userInput.lower()[0:6] == "runapp":

                run_app(userInput)


            elif userInput.lower()[0:7] == "stopapp":

                stop_app(userInput)

                print("Stopped {}".format(userInput[8::]))


            elif userInput.lower() == "wakeup":

                wake_up()

                time.sleep(1)

                print("Success")


            elif userInput.lower() == "sleep":

                sleep()

                print("Success")



            elif userInput.lower() == "shutdown":

                shutdown()

                time.sleep(1)

                print("Success")


            elif userInput.lower() == "right":

                right()



            elif userInput.lower() == "left":

                left()


            elif userInput.lower() == "up":

                up()


            elif userInput.lower() == "down":

                down()


            elif userInput.lower() == "screencap":

                screenshot()

                print("Successfully")


            elif userInput.lower()[0:7] == "clearapp":

                clear_app(userInput)

                print("Success")


            elif userInput.lower() == "takepic":

                take_pic()

                print("Success")


            elif userInput.lower() == "browser":

                browser()

                print("Success")


            elif userInput.lower() == "resume":

                resume()

                print("Success")


            elif userInput.lower() == "pause":

                pause()

                print("Success")


            elif userInput.lower() == "mute":

                mute()

                print("Success")


            elif userInput.lower() == "getmodel":

                get_model()


            elif userInput.lower() == "getbattery":

                print()
                get_battery()
                print()


            elif userInput.lower() == "getsize":

                getsize()


            elif userInput.lower() == "getid":

                get_id()


            elif userInput.lower() == "getversion":

                get_version()


            elif userInput.lower() == "ifconfig":

                print()

                ifconfig()

                print()



            elif userInput.lower() == "getmac":

                get_mac()

                print()


            elif userInput.lower() == "cpuinfo":

                print()

                cpu_info()

                print()


            elif userInput.lower() == "meminfo":

                print()

                mem_info()

                print()


            elif userInput.lower()[0:4] == "pull":

                    pull(userInput)

                    print("Success")


            elif userInput.lower()[0:4] == "push":

                    push(userInput)

                    print("Success")


            elif userInput.lower() == "screenrec":

                path = "/sdcard/sc.mp4" ##### change here if you want to save elsewhere #####

                screen_record(path)

                print("Success")

                print("You can get the video with the pull command from " + path)
                

            elif userInput.lower() == "livescreen":

                live_screen()


            elif userInput.lower() == "assistant":
                
                assistant()

                print("Success")


            elif userInput.lower() == "ps":

                print()

                os.system("adb shell ps")

                print()


            elif userInput.lower() == "top":

                print()

                os.system("adb shell top")

                print()


            elif userInput.lower()[0:2] == "cat":

                splitinput2 = userInput.split(" ")

                os.system("adb shell cat {}".format(splitinput2[1]))

                print()


            elif userInput.lower()[0:1] == "cd":

                splitinput3 = userInput.split(" ")

                os.system("adb shell cd {}".format(splitinput3[1]))

                print()


            elif userInput.lower()[0:1] == "ls":

                splitinput4 = userInput.split(" ")

                os.system("adb shell ls {}".format(splitinput4[1]))

                print()


            elif userInput.lower()[0:1] == "mv":

                splitinput5 = userInput.split(" ")

                os.system("adb shell mv {} {}".format(splitinput5[1], splitinput5[2]))

                print()


            elif userInput.lower() == "help":

                print(helpMenu)



            elif userInput.lower() == "exit":

                print("Closing...")

                time.sleep(0.4)

                sys.exit()


            else:

                print("[+] Incorrect Entry Please see help page")


    except KeyboardInterrupt:

            print('\nClosing...')

            time.sleep(0.4)

            sys.exit()


try:

    check_adb = subprocess.check_output("which adb",shell=True).decode('utf-8')

except:

    print("Error : adb not found in path")

    sys.exit()


adbDevicesOutput = subprocess.check_output("adb devices", shell=True).decode('utf-8')


if len(adbDevicesOutput) == 26:

    print("Error: connected device not found!")

    sys.exit()


else:

    print("Connected! ")

    print()

    while True:

        main()
        


##Functions##

