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

def send(signal, value):
    """This method will be overloaded by the plugin"""
    pass

class TestSender(unittest.TestCase):

    def setUp(self):
        print(self._testMethodName)
        load_plugin('ipc.zeromq')

    def test_sender(self):
        # Send signals with different value types.
        for signal in [ "car.backup" , "volume.up" , "car.stop" ]:
            send(signal, None)
            print("sent:", signal)

if __name__ == '__main__':
    unittest.main()
