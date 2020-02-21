#! /usr/bin/python

#imports
import time
import requests
import subprocess
import os
import datetime


def is_service_running(name):
    with open(os.devnull, 'wb') as hide_output:
        exit_code = subprocess.Popen(['service', name, 'status'], stdout=hide_output, stderr=hide_output).wait()
        return exit_code == 0

while True:

    if is_service_running('dbus-fi.w1.wpa_supplicant1'): #default
        
        currentTime = datetime.datetime.now()
        response = requests.post("https://maker.ifttt.com/trigger/<something>/with/key/<somekey>", params={"value1": str(currentTime.strftime("%H:%M:%S"))})
        break
