# flake8-in-file-ignores: noqa: F401,F403,F405

# Copyright (c) 1994 Adam Karpierz
# SPDX-License-Identifier: Zlib

from ._platform import *

if is_windows:  # pragma: no cover
    from ._windows import DLL_PATH, DLL, dlclose, CFUNC
elif is_linux:  # pragma: no cover
    from ._linux import DLL_PATH, DLL, dlclose, CFUNC
elif is_macos:  # pragma: no cover
    from ._macos import DLL_PATH, DLL, dlclose, CFUNC
else:  # pragma: no cover
    raise ImportError("unsupported platform")
