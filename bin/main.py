#!/usr/bin/env python3
'''Copyright (C) 2017 Collabora
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Authors: Shane Fagan - shane.fagan@collabora.com
'''

import datetime
import sys
import os
from time import sleep
from threading import Thread
sys.path.append(os.path.dirname(__file__))
RULES_PATH = os.path.abspath(os.path.join('..', 'rules', 'simple'))


class Main():
    '''
        Class to handle states
    '''
    def __init__(self):
        pass


def __log_message(message):
    '''
        Internal logging for debug
    '''
    with open("messages.log", "a", encoding="utf-8") as f:
        message = "{} %% {}\n".format(datetime.datetime.now(), message)
        f.write(message)
        f.flush()
        print(message)


def run():
    '''
        Loop to grab logic from stdin, then spawn a threads for processing
    '''
    for line in sys.stdin:
        line = line.replace(" ", "").strip('\n')
        if line == "":
            # Ignore blank lines
            pass
        if line == "quit":
            break
        elif "=" in line:
            line = line.split("=")
            Thread(target=process, args=(line[0], line[1])).start()
        else:
            Thread(target=process, args=(line, None)).start()

def process(signal, value):
    '''
        Handle the emitting of singals and adding values to state
    '''
    # from str to int or float (if that is needed)
    if type(value) == 'str' and value.isalnum():
        if '.' in value:
            value = float(value)
        else:
            value = int(value)

    if value is not None:
        # If it's an assignment do it
        __log_message("{} = {}".format(signal, value))
        vars(main)[signal] = value
    else:
        # Else run the method
        __log_message("{}".format(signal))

def process_delay(signal, value, delay):
    '''
        Process with a delay in ms
    '''
    sleep(delay/1000)
    process(signal, value)


if __name__ == "__main__":
    main = Main()
    run()
