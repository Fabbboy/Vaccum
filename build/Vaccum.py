#!/usr/bin/env python
# prompt written in python3
import hashlib
import json
import random
from datetime import datetime

from translate import Translator

now = datetime.now()

import os


def startup():
    if not os.path.isfile('config.json'):
        with open('config.json', 'w') as outfile:
            json.dump({
                "_comment": "keyword: $time, $date, $version, $prefix, $valid, $sha256",
                "version": "2.1.0",
                "prefix": "[Vaccum $version] >>>",
                "clearOnRun": "True",
                "welcomeMessage": "\n┏ Welcome to the Vaccum prompt ┓\n┃Date: $date        ┃\n┃Time: $time                ┃\n┃Version: $version                ┃\n┃Prefix: $prefix ┃\n┃License: $valid                ┃\n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛",
                "info": "blue",
                "error": "red",
                "showExtensions": "$endMost: [$yellow$ext$end]",
            }, outfile)
    f = open("config.json", "r")
    config = json.load(f)

    if bool(config["clearOnRun"]):
        os.system('clear')
    welM = config["welcomeMessage"]
    # keyword: $time, $date, $version, $prefix, $valid
    welM = welM.replace("$time", now.strftime("%H:%M:%S"))
    welM = welM.replace("$date", now.strftime("%D:%m:%Y"))
    welM = welM.replace("$version", config["version"])
    welM = welM.replace("$prefix", config["prefix"])
    welM = welM.replace("$valid", "Valid")
    # welM = welM.replace("$license", config["license"])
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

    while True:
        ex = config["showExtensions"]
        ex = ex.replace("$ext", getMostUsedExtension())
        ex = ex.replace("$red", "\033[91m")
        ex = ex.replace("$green", "\033[92m")
        ex = ex.replace("$yellow", "\033[93m")
        ex = ex.replace("$blue", "\033[94m")
        ex = ex.replace("$magenta", "\033[95m")
        ex = ex.replace("$cyan", "\033[96m")
        ex = ex.replace("$white", "\033[97m")
        ex = ex.replace("$end", "\033[0m")
        ex = ex.replace("$time", now.strftime("%H:%M:%S"))
        ex = ex.replace("$date", now.strftime("%D:%m:%Y"))
        ex = ex.replace("$version", config["version"])
        ex = ex.replace("$prefix", config["prefix"])
        ex = ex.replace("$valid", "Valid")
        ex = ex.replace("$sha256", encode("Vaccum", "sha256"))
        print(ex)

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
                config["prefix"] = cmd_list[1]
            else:
                print("prefix is empty")
            # safe config
            with open("config.json", "w") as f:
                json.dump(config, f)
            continue
        if cmd_list[0] == "encode":
            if len(cmd_list) > 1:
                out = encode(cmd_list[2], cmd_list[1])
                print(out)
            continue
            continue
        if cmd_list[0] == "time":
            print(now)
            continue
        # check if cmd_list[0] == "cd"
        if cmd_list[0] == "cd":
            if len(cmd_list) > 1:
                # check if folder exist called cmd_list[1]
                if os.path.lexists(cmd_list[1]):
                    if os.path.isdir(cmd_list[1]):
                        os.chdir(cmd_list[1])
                    continue
                else:
                    exception("Folder does not exist", False)
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


def exception(message, exit):
    # check if exit is true
    with open('config.json') as data_file:
        config = json.load(data_file)
    if exit:
        # print message in red
        if config["error"] == "red":
            print("\033[91m" + "[ERROR] " + message + "\033[0m")
        elif config["error"] == "blue":
            print("\033[94m" + "[ERROR] " + message + "\033[0m")
        elif config["error"] == "green":
            print("\033[92m" + "[ERROR] " + message + "\033[0m")
        elif config["error"] == "yellow":
            print("\033[93m" + "[ERROR] " + message + "\033[0m")
        elif config["error"] == "white":
            print("\033[97m" + "[ERROR] " + message + "\033[0m")
        elif config["error"] == "black":
            print("\033[90m" + "[ERROR] " + message + "\033[0m")
        elif config["error"] == "magenta":
            print("\033[95m" + "[ERROR] " + message + "\033[0m")
        elif config["error"] == "cyan":
            print("\033[96m" + "[ERROR] " + message + "\033[0m")
        elif config["error"] == "grey":
            print("\033[90m" + "[ERROR] " + message + "\033[0m")
        else:
            print("\033[91m" + "[ERROR] " + message + "\033[0m")

        # exit program
        exit()
    else:
        # print message in red
        print("\033[91m" + "[ERROR] " + message + "\033[0m")


def info(message, pre):
    # print message in blue color
    # open config.json file

    with open('config.json') as data_file:
        config = json.load(data_file)
    if pre:
        if config["info"] == "blue":
            print("\033[94m" + "[INFO] " + message + "\033[0m")
        elif config["info"] == "green":
            print("\033[92m" + "[INFO] " + message + "\033[0m")
        elif config["info"] == "red":
            print("\033[91m" + "[INFO] " + message + "\033[0m")
        elif config["info"] == "yellow":
            print("\033[93m" + "[INFO] " + message + "\033[0m")
        elif config["info"] == "white":
            print("\033[97m" + "[INFO] " + message + "\033[0m")
        elif config["error"] == "black":
            print("\033[90m" + "[INFO] " + message + "\033[0m")
        elif config["error"] == "magenta":
            print("\033[95m" + "[INFO] " + message + "\033[0m")
        elif config["error"] == "cyan":
            print("\033[96m" + "[INFO] " + message + "\033[0m")
        elif config["error"] == "grey":
            print("\033[90m" + "[INFO] " + message + "\033[0m")
        else:
            print("\033[94m" + "[INFO] " + message + "\033[0m")
    else:
        if config["info"] == "blue":
            print("\033[94m" + message + "\033[0m")
        elif config["info"] == "green":
            print("\033[92m" + message + "\033[0m")
        elif config["info"] == "red":
            print("\033[91m" + message + "\033[0m")
        elif config["info"] == "yellow":
            print("\033[93m" + message + "\033[0m")
        elif config["info"] == "white":
            print("\033[97m" + message + "\033[0m")
        elif config["error"] == "black":
            print("\033[90m" + message + "\033[0m")
        elif config["error"] == "magenta":
            print("\033[95m" + message + "\033[0m")
        elif config["error"] == "cyan":
            print("\033[96m" + message + "\033[0m")
        elif config["error"] == "grey":
            print("\033[90m" + message + "\033[0m")
        else:
            print("\033[94m" + message + "\033[0m")


def encode(msg, algo):
    if algo == "md5":
        return hashlib.md5(msg.encode()).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(msg.encode()).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(msg.encode()).hexdigest()
    elif algo == "sha512":
        return hashlib.sha512(msg.encode()).hexdigest()
    else:
        return "Invalid algorithm"


def getMostUsedExtension():
    # get all files in directory
    files = os.listdir(os.getcwd())
    # get file extension and find the extension used the most ignore folders and hidden files
    extension = {}
    for file in files:
        if file.startswith('.'):
            continue
        if os.path.isdir(file):
            continue
        if '.' in file:
            extension[file.split('.')[1]] = extension.get(file.split('.')[1], 0) + 1
    # return the extension used the most
    # if there is no extension return None
    if len(extension) == 0:
        return str(None)
    else:
        return max(extension, key=extension.get)

    return mostUsedExtension


if __name__ == "__main__":
    startup()
