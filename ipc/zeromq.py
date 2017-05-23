#
#  Copyright (C) 2017, Collabora Ltd.
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this file,
#  You can obtain one at http://mozilla.org/MPL/2.0/.
#

import os
import zmq
import os.path

IPC_SOCKET_PATH = os.path.join(os.environ['XDG_RUNTIME_DIR'], "vsm-ipc.socket")
IPC_SOCKET = "ipc://{}".format(IPC_SOCKET_PATH)

def _send(signal, value):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(IPC_SOCKET)

    # Send Python tuple: (Signal ID, Signal Value).
    socket.send_pyobj((signal, value))

    # Wait for receiver reply.
    socket.recv()

def _receive():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(IPC_SOCKET)

    # Receive Python object: (Signal ID, Signal Value).
    msg = socket.recv_pyobj()

    # Send 1 byte as a reply to the client.
    socket.send(bytes(1))
    return msg

#
# The module public interface consists of the following functions:
#
# send    - Function to send signal
# receive - Function that receives signal.
#           It returns the received message as a tuple of (ID, Value).
#
def send(signal, value):
    _send(signal, value)

def receive():
    return _receive()
