#!/usr/bin/env python3.5m
#
#   Copyright (C) 2017, Collabora Ltd.
#
#   This Source Code Form is subject to the terms of the Mozilla Public
#   License, v. 2.0. If a copy of the MPL was not distributed with this file,
#   You can obtain one at http://mozilla.org/MPL/2.0/.
#

import importlib

class PluginLoader(object):
    """
    This class loads a module to accept and receive signals.

    It creates a PluginLoader object that offers access to the following
    methods of the loaded module:

    receive_signal - Method to receive signal
    send_signal    - Method to send signal
    """

    def __init__(self, modulename):
        self._module = self._load_module(modulename)

    def _load_module(self, modulename):
        try:
            return importlib.import_module(modulename)
        except ImportError:
            print("Error loading module: {}".format(modulename))
            raise

    def receive_signal(self):
        """
        Method to receive signal.
        It returns the received message as a tuple of (ID, Value).
        """
        return self._module.receive_signal()

    def send_signal(self, sigid, sigvalue):
        """
        Method to send signal.
        It takes the signal ID and Value as arguments.
        """
        self._module.send_signal(sigid, sigvalue)
