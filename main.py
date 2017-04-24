import os
import json
from sys import exit
from time import sleep
from distutils.dir_util import copy_tree


def readJson(filename):
    with open(filename) as data:
        return json.load(data)


def getFiles(dir):
    file_paths = []

    for root, dirs, files in os.walk(dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


def copyDir(src, dist):
    copy_tree(src, dist)


def infileReplace(filename, oldString, newString):
    with open(filename) as f:
        s = f.read()

        if oldString not in s:
            return

    with open(filename, 'w') as f:
        s = s.replace(oldString, newString)
        f.write(s)


def replaceValuesInPath(pathname, values, separator):
    for file in getFiles(pathname):
        for item in values:
            replaceKey = separator[0] + str.upper(item) + separator[1]
            replaceValue = values[item]

            infileReplace(file, replaceKey, replaceValue)


"""
    Init Program
"""

jsonFile = 'meta.json'

if not os.path.isfile(jsonFile):
    print(jsonFile + " file is missing")
    sleep(3)
    exit()

json_data = readJson(jsonFile)
inputFolder = json_data["config"]["input"]
outputFolder = json_data["config"]["output"]
separator = json_data["config"]["separator"]

if not os.path.isdir(inputFolder):
    print(inputFolder + " folder is missing")
    sleep(3)
    exit()

del json_data["config"]

copyDir(inputFolder, outputFolder)
replaceValuesInPath(outputFolder, json_data, separator)

print("Done! Good lucky")
sleep(2)
exit()
