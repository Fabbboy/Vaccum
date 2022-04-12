# get all files in directory get file extension and find the extension used the most
import os


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
    return max(extension, key=extension.get)

    return mostUsedExtension

