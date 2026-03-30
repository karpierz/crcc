# Copyright (c) 1994 Adam Karpierz
# SPDX-License-Identifier: Zlib

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class BuildExt(build_ext):

    cc_args_map = {
        "msvc": ["/O2", "/WX", "/wd4996"],
        "unix": ["-O3", "-g0", "-ffast-math"],
    }
    ld_args_map = {
        "msvc": ["/DEF:src/crcc/crc.c/crc.def"],
        "unix": [],
    }

    def build_extension(self, ext: Extension):
        cc_type = self.compiler.compiler_type
        cc_args = self.cc_args_map.get(cc_type,
                                       self.cc_args_map["unix"])
        ld_args = self.ld_args_map.get(cc_type,
                                       self.ld_args_map["unix"])
        if cc_type == "msvc":
            pass
        elif cc_type == "unix":
            pass
        ext.extra_compile_args = cc_args
        ext.extra_link_args = ld_args
        super().build_extension(ext)

ext_modules = [
    Extension(
        name="crcc._platform.crc",
        language="c",
        sources=["src/crcc/crc.c/crc.c",
                 "src/crcc/crc.c/crc_table.c",
                 "src/crcc/crc.c/crc_update.c",
                 "src/crcc/crc.c/crc_py.c"],
        depends=["include/crcc/crc.h",
                 "src/crcc/crc.c/crc.def",
                 "src/crcc/crc.c/crc_defs.h",
                 "src/crcc/crc.c/crc_table.h",
                 "src/crcc/crc.c/crc_update.h"],
        include_dirs=["include"],
    ),
]

setup(
    ext_modules = ext_modules,
    cmdclass = dict(build_ext=BuildExt),
)
