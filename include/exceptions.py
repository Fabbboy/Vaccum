import json


def exception(message, exit):
    #check if exit is true
    with open('config.json') as data_file:
        config = json.load(data_file)
    if exit:
        #print message in red
        if config["error"] == "red":
              print("\033[91m"+ "[ERROR] " + message + "\033[0m")
        elif config["error"] == "blue":
              print("\033[94m"+ "[ERROR] " + message + "\033[0m")
        elif config["error"] == "green":
              print("\033[92m"+ "[ERROR] " + message + "\033[0m")
        elif config["error"] == "yellow":
              print("\033[93m"+ "[ERROR] " + message + "\033[0m")
        elif config["error"] == "white":
              print("\033[97m"+ "[ERROR] " + message + "\033[0m")
        elif config["error"] == "black":
              print("\033[90m"+ "[ERROR] " + message + "\033[0m")
        elif config["error"] == "magenta":
              print("\033[95m"+ "[ERROR] " + message + "\033[0m")
        elif config["error"] == "cyan":
              print("\033[96m"+ "[ERROR] " + message + "\033[0m")
        elif config["error"] == "grey":
              print("\033[90m"+ "[ERROR] " + message + "\033[0m")
        else:
              print("\033[91m"+ "[ERROR] " + message + "\033[0m")

        #exit program
        exit()
    else:
        #print message in red
        print("\033[91m" + "[ERROR] " + message + "\033[0m")
