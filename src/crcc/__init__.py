# flake8-in-file-ignores: noqa: F401,F403,F821

# Copyright (c) 1994 Adam Karpierz
# SPDX-License-Identifier: Zlib

"""Python API of CRC package."""

from .__about__ import * ; del __about__  # type: ignore[name-defined]

from ._crc import * ; del _crc  # type: ignore[name-defined]
