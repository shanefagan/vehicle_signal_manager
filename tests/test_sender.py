#!/usr/bin/env python3.5m
#
#   Copyright (C) 2017, Collabora Ltd.
#
#   This Source Code Form is subject to the terms of the Mozilla Public
#   License, v. 2.0. If a copy of the MPL was not distributed with this file,
#   You can obtain one at http://mozilla.org/MPL/2.0/.
#

import sys
import unittest
import numpy as np
sys.path.append('..')
from ipc_plugin.plugin_loader import PluginLoader

class TestSender(unittest.TestCase):

    def setUp(self):
        print(self._testMethodName)
        self.send_signal = PluginLoader('ipc_plugin.ipc_mod').send_signal

    def test_sender(self):
        # Send signals with different value types.
        self.send_signal(int(105), np.uint8(98))
        self.send_signal(int(8), np.int8(89))
    
        self.send_signal(int(29), np.uint16(35))
        self.send_signal(int(10657), np.int16(90))

        self.send_signal(int(923), np.uint32(763554))
        self.send_signal(int(108), np.int32(-9872))

        self.send_signal(int(543), np.uint64(98725830))
        self.send_signal(int(10005), np.int64(-3426614))
    
        self.send_signal(int(178), True)

        self.send_signal(int(465), np.float32(129.23664))
        self.send_signal(int(300), np.float64(143.283664))

        self.send_signal(int(102), "front_left")
        self.send_signal(int(178), bytes(9))

if __name__ == '__main__':
    unittest.main()
