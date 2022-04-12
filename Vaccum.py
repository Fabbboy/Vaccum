#!/usr/bin/env python
# prompt written in python3
import json
import random
from datetime import datetime
from translate import Translator
now = datetime.now()

from include.sha256 import sha256
from include.exceptions import *
from include.info import *
import os

def startup():
    if not os.path.isfile('config.json'):
        with open('config.json', 'w') as outfile:
            json.dump({
                "_comment": "keyword: $time, $date, $version, $prefix, $valid, $sha256",
                "version": "1.0.0",
                "prefix": "[Vaccum $version] >>>",
                "clearOnRun": "True",
                "welcomeMessage": "\n┏ Welcome to the Vaccum prompt ┓\n┃Date: $date        ┃\n┃Time: $time                ┃\n┃Version: $version                ┃\n┃Prefix: $prefix ┃\n┃License: $valid                ┃\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛",
                "info": "blue",
                "error": "red"
            }, outfile)
    f = open("config.json", "r")
    config = json.load(f)
    if bool(config["clearOnRun"]):
         os.system('clear')
    welM = config["welcomeMessage"]
    # keyword: $time, $date, $version, $prefix, $valid, $red
    welM = welM.replace("$time", now.strftime("%H:%M:%S"))
    welM = welM.replace("$date", now.strftime("%D:%m:%Y"))
    welM = welM.replace("$version", config["version"])
    welM = welM.replace("$prefix", config["prefix"])
    welM = welM.replace("$valid", "Valid")
    welM = welM.replace("$sha256", sha256("Vaccum"))
    trans = Translator(config["lang"])
    info(trans.translate(welM), False)
    prompt()


def prompt():
    # check if config.json exists and if not create it

    f = open("config.json", "r")
    config = json.load(f)

    pref = config["prefix"]
    pref = pref.replace("$time", now.strftime("%H:%M:%S"))
    pref = pref.replace("$date", now.strftime("%D:%m:%Y"))
    pref = pref.replace("$version", config["version"])
    pref = pref.replace("$prefix", config["prefix"])
    pref = pref.replace("$valid", "Valid")
    pref = pref.replace("$sha256", sha256("Vaccum"))
    pref = pref.replace("$red", "\033[91m")
    pref = pref.replace("$green", "\033[92m")
    pref = pref.replace("$yellow", "\033[93m")
    pref = pref.replace("$blue", "\033[94m")
    pref = pref.replace("$magenta", "\033[95m")
    pref = pref.replace("$cyan", "\033[96m")
    pref = pref.replace("$white", "\033[97m")
    pref = pref.replace("$end", "\033[0m")

    while True:
        cmd = input(f'{pref} ')
        # split cmd into list
        cmd_list = cmd.split()
        # check if cmd_list[] is empty
        if len(cmd_list) == 0:
            cmd_list.append("\n")
        # check if cmd_list[1] is out of range
        if len(cmd_list) > 1:
            cmd_list.append("\n")
        # check if cmd_list[0] is "reEnter"
        if cmd_list[0] == "reEnter" or cmd_list[0] == "reenter":
            startup()
        # check if cmd_list[0] == "exit"

        if cmd_list[0] == "exit":
            # exit the program
            # print sha256 string with the current time
            print("Transaction: " + sha256(str(now)))
            exit(0)
            break

        # check if cmd_list[0] == "Clear"
        if cmd_list[0] == "prefix":
            # set config["prefix"] to cmd_list[1] if cmd_list[1] is not empty
            if len(cmd_list) > 1:
                config["prefix"] = cmd_list[1]
            else:
                print("prefix is empty")
            # safe config
            with open("config.json", "w") as f:
                json.dump(config, f)
            continue
        if cmd_list[0] == "sha256":
            if len(cmd_list) > 1:
                if cmd_list[1] == "random" or cmd_list[1] == "r":
                    print("" + str(sha256(str(random.randint(0, 10000)))))
                else:
                    print("" + sha256(cmd_list[1]))
            continue
        if cmd_list[0] == "time":
            print(now)
            continue
        #check if cmd_list[0] == "cd"
        if cmd_list[0] == "cd":
            if len(cmd_list) > 1:
                os.chdir(cmd_list[1])
            continue
        else:
            # check if cmd is nano
            if cmd_list[0] == 'nano':
                # check if file is valid
                if len(cmd_list) == 2:
                    # check if file is valid
                    if os.path.isfile(cmd_list[1]):
                        # open file
                        os.system('nano ' + cmd_list[1])
                    else:
                        print('Error: No such file or directory')
                else:
                    print('Error: Invalid number of arguments')
            os.system(cmd)
            #prompt()

if __name__ == "__main__":
    startup()
