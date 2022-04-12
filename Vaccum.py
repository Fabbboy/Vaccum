#!/usr/bin/env python
# prompt written in python3
import json
import random
from datetime import datetime
from translate import Translator

now = datetime.now()

from include.readDir import getMostUsedExtension
from include.encode import encode
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
                "welcomeMessage": "\n┏ Welcome to the Vaccum prompt ┓\n┃Date: $date        ┃\n┃Time: $time            "
                                  "    ┃\n┃Version: $version                ┃\n┃Prefix: $prefix ┃\n┃License: $valid   "
                                  "             ┃\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛",
                "info": "blue",
                "error": "red",
                "showExtensions": "True",
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
    welM = welM.replace("$sha256", encode("Vaccum", "sha256"))
    welM = welM.replace("$path", os.getcwd())
    info(welM, False)
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
    pref = pref.replace("$sha256", encode("Vaccum", "sha256"))
    pref = pref.replace("$red", "\033[91m")
    pref = pref.replace("$green", "\033[92m")
    pref = pref.replace("$yellow", "\033[93m")
    pref = pref.replace("$blue", "\033[94m")
    pref = pref.replace("$magenta", "\033[95m")
    pref = pref.replace("$cyan", "\033[96m")
    pref = pref.replace("$white", "\033[97m")
    pref = pref.replace("$end", "\033[0m")
    pref = pref.replace("$ext", getMostUsedExtension())
    pref = pref.replace("$path", os.getcwd())

    while True:
        if bool(config["showExtensions"]):
            ext = getMostUsedExtension()
            info(ext, False)
        cmd = input(f'{pref} ')
        #check if "showExtensions" is true
        # split cmd into list
        cmd_list = cmd.split()
        # check if cmd_list[] is empty
        if len(cmd_list) == 0:
            cmd_list.append("\n")
        # check if cmd_list[1] is out of range
        if len(cmd_list) > 1:
            cmd_list.append("\n")
        # check if cmd_list[0] is "reEnter"
        if cmd_list[0] == "reload":
            startup()
        # check if cmd_list[0] == "exit"

        if cmd_list[0] == "exit":
            # exit the program
            # print sha256 string with the current time
            print("Transaction: " + encode(str(now), "sha256"))
            exit(0)
            break

        # check if cmd_list[0] == "Clear"
        if cmd_list[0] == "prefix":
            # set config["prefix"] to cmd_list[1] if cmd_list[1] is not empty
            if len(cmd_list) > 1:
                # set config["prefix"] to all the elements of cmd_list after the first element
                config["prefix"] = " ".join(cmd_list[1:])
                # if the last char is a \n remove it
                if config["prefix"][-1] == "\n":
                    config["prefix"] = config["prefix"][:-1]

                # write config.json
                with open('config.json', 'w') as outfile:
                    json.dump(config, outfile)
            else:
                print("prefix is empty")
            # safe config
            with open("config.json", "w") as f:
                json.dump(config, f)
            continue
        if cmd_list[0] == "encode":
            if len(cmd_list) > 1:
                print(encode(cmd_list[2], cmd_list[1]))
            continue
        if cmd_list[0] == "time":
            print(now)
            continue
        # check if cmd_list[0] == "cd"
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
            # prompt()


if __name__ == "__main__":
    startup()
