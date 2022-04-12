import json


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

