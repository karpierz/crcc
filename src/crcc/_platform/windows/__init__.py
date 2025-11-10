# flake8-in-file-ignores: noqa: E402,N813,N814

# Copyright (c) 1994 Adam Karpierz
# SPDX-License-Identifier: Zlib

from typing import Any
import ctypes
import sysconfig
from pathlib import Path

__all__ = ('DLL_PATH', 'DLL', 'dlclose', 'CFUNC')

this_dir = Path(__file__).resolve().parent
dll_suff = sysconfig.get_config_var("EXT_SUFFIX") or ".pyd"

DLL_PATH = this_dir.parent/("crc" + dll_suff)

from ctypes import WinDLL as _DLL
try:
    from _ctypes import FreeLibrary as dlclose
except ImportError:  # pragma: no cover
    dlclose = lambda handle: None
from ctypes import CFUNCTYPE as CFUNC

def DLL(*args: Any, **kwargs: Any) -> ctypes.CDLL:
    import os
    with os.add_dll_directory(os.path.dirname(args[0])):
        return _DLL(*args, **kwargs)
