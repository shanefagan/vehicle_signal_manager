#!/usr/bin/env python3.5m
#
#  Copyright (C) 2017, Jaguar Land Rover
#
#  This program is licensed under the terms and conditions of the
#  Mozilla Public License, version 2.0.  The full text of the 
#  Mozilla Public License is at https://www.mozilla.org/MPL/2.0/
#

import unittest
from ipc.loader import load_plugin

def receive():
    """This method will be overloaded by the plugin"""
    pass

class TestReceiver(unittest.TestCase):

    def setUp(self):
        print(self._testMethodName)
        load_plugin('ipc.zeromq')

    def test_receiver(self):
        i = 0
        while i < 3:
            signal, value = receive()
            print("received: {} , {}".format(signal, value))
            i += 1

if __name__ == '__main__':
    unittest.main()
