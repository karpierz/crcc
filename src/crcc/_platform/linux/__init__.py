# flake8-in-file-ignores: noqa: E402

# Copyright (c) 1994 Adam Karpierz
# SPDX-License-Identifier: Zlib

import ctypes
import sysconfig
from pathlib import Path
from functools import partial

__all__ = ('DLL_PATH', 'DLL', 'dlclose', 'CFUNC')

this_dir = Path(__file__).resolve().parent
dll_suff = sysconfig.get_config_var("EXT_SUFFIX") or ".pyd"

DLL_PATH = this_dir.parent/("crc" + dll_suff)

from ctypes  import CDLL as _DLL
from _ctypes import dlclose  # type: ignore[attr-defined]
from ctypes  import CFUNCTYPE as CFUNC

DLL = partial(_DLL, mode=ctypes.RTLD_GLOBAL)
