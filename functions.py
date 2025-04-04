from log import authLog

import traceback
import time
import csv
import re
import os

def checkIsDigit(input_str):
    from log import authLog
    try:
        authLog.info(f"String successfully validated selection number {input_str}, from checkIsDigit function.")
        return input_str.strip().isdigit()
    
    except Exception as error:
        pass
        authLog.error(f"Invalid option chosen: {input_str}, error: {error}")
        authLog.error(traceback.format_exc())

def checkYNInput(stringInput):
    return stringInput.lower() == 'y' or stringInput.lower() == 'n'

def logInCSV(validDeviceIP, filename="", *args):
    print(f"INFO: File created: {filename}")
    with open(f'Outputs/{filename}.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([validDeviceIP, *args])
        authLog.info(f"Appended device: {validDeviceIP} to file {filename}")

def genTxtFile(validDeviceIP, username, filename="", *args):
    with open(f"Outputs/{validDeviceIP} {filename}.txt","a") as failedDevices:
        failedDevices.write(f"User {username} connected to {validDeviceIP}\n\n")
        for arg in args:
            if isinstance(arg, dict):
                for key,values in arg.items():
                    failedDevices.write(f"{key}: ")
                    failedDevices.write(", ".join(str(v) for v in values))
                    failedDevices.write("\n")
            
            elif isinstance(arg, list):
                for item in arg:
                    failedDevices.write(item)
                    failedDevices.write("\n")

            elif isinstance(arg, str):
                failedDevices.write(arg + "\n")

def addToList(deviceIP, generalList, *args):
    for item in args:
        if isinstance(item,list):
            generalList.extend(item)
            authLog.info(f"Item: {item} appended to list 'commandOutput' for device: {deviceIP}")
        else:
            print(f"ERROR: A list wasn't received.")
            authLog.info(f"A list wasn't received.")

def cleanAddress(address, file):
    authLog.info(f"Address: {address} entered the cleanAddress function from file: {file}")
    originalAddress = address
    address = re.sub(r'Suite\s*\d+', '', address, flags=re.I)
    address = re.sub(r'\s+', ' ', address).strip()
    authLog.info(f"Original address was modified from: {originalAddress}, to new address: {address}, from file: {file}")
    return address