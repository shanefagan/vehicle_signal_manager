#!/usr/bin/env python3.5m
#
#   Copyright (C) 2017, Collabora Ltd.
#
#   This Source Code Form is subject to the terms of the Mozilla Public
#   License, v. 2.0. If a copy of the MPL was not distributed with this file,
#   You can obtain one at http://mozilla.org/MPL/2.0/.
#

import zmq

IPC_SOCKET = "ipc:///tmp/vsi.ipc"

class SignalSender(object):
    """Class to send IPC signals."""

    def __init__(self):
        context = zmq.Context()
        self._socket = context.socket(zmq.REQ)
        self._socket.connect(IPC_SOCKET)

    def send(self, sigid, sigvalue):
        # Send a Python tuple.
        # First element is the signal ID and second element is the signal value.
        self._socket.send_pyobj((sigid, sigvalue))
        # Wait for receiver reply.
        self._socket.recv()

class SignalReceiver(object):
    """Class to receive IPC signals."""

    def __init__(self):
        context = zmq.Context()
        self._socket = context.socket(zmq.REP)
        self._socket.bind(IPC_SOCKET)

    def receive(self):
        msg = self._socket.recv_pyobj()
        # Send 1 byte as a reply to the client.
        self._socket.send(bytes(1))
        return msg

#
# The module public interface consists of the following functions:
#
# receive_signal - Function that receives signal.
#                  It returns the received message as a tuple of (ID, Value).
# send_signal    - Function to send signal
#
def receive_signal():
    return SignalReceiver().receive()

def send_signal(sigid, sigvalue):
    SignalSender().send(sigid, sigvalue)
