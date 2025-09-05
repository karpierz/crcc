# flake8-in-file-ignores: noqa: E402,F401

# Copyright (c) 1994 Adam Karpierz
# SPDX-License-Identifier: Zlib

import sys
import os
import platform
import sysconfig
import ctypes as ct
from functools import partial

from utlx.platform import is_pypy

__all__ = ('DLL_PATH', 'DLL', 'dlclose', 'CFUNC')

this_dir = os.path.dirname(os.path.abspath(__file__))

dll_suffix = (("" if is_pypy
               or not ((3, 0) <= sys.version_info[:2] <= (3, 7))
               else ("." + platform.python_implementation()[:2].lower()
               + sysconfig.get_python_version().replace(".", "") + "-"
               + sysconfig.get_platform().replace("-", "_")))
              + (sysconfig.get_config_var("EXT_SUFFIX") or ".pyd"))

DLL_PATH = os.path.join(os.path.dirname(this_dir), "crc" + dll_suffix)

from ctypes  import CDLL as _DLL
from _ctypes import dlclose  # type: ignore[attr-defined]
from ctypes  import CFUNCTYPE as CFUNC

DLL = partial(_DLL, mode=ct.RTLD_GLOBAL)
