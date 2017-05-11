#
#  Copyright (C) 2017, Jaguar Land Rover
#
#  This program is licensed under the terms and conditions of the
#  Mozilla Public License, version 2.0.  The full text of the 
#  Mozilla Public License is at https://www.mozilla.org/MPL/2.0/
#

import inspect
import importlib

def _load_module(modulename):
    try:
        return importlib.import_module(modulename)
    except ImportError:
        print("Error loading module: {}".format(modulename))
        raise

def _exist_method(module, method):
    return hasattr(module, method) and inspect.isroutine(getattr(module, method))

def load_plugin(modulename):
    # Load plugin module.
    module = _load_module(modulename)

    # Inspect caller module.
    caller_info = inspect.stack()[1]
    caller_module = inspect.getmodule(caller_info[0])

    # Override receive/send functions _only_ if they both exist
    # in the caller and plugin module.
    if _exist_method(caller_module, 'receive') and \
       _exist_method(module, 'receive'):
        caller_module.receive = module.receive

    if _exist_method(caller_module, 'send') and _exist_method(module, 'send'):
        caller_module.send = module.send
