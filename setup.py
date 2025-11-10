# Copyright (c) 1994 Adam Karpierz
# SPDX-License-Identifier: Zlib

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class BuildExt(build_ext):

    compile_args = {
        "msvc": ["/O2", "/WX", "/wd4996"],
        "unix": ["-O3", "-g0", "-ffast-math"],
    }
    link_args = {
        "msvc": ["/DEF:src/crcc/crc.def"],
        "unix": [],
    }

    def build_extensions(self):
        cc_type = self.compiler.compiler_type
        compile_args = self.compile_args.get(cc_type, self.compile_args["unix"])
        link_args    = self.link_args.get(cc_type, self.link_args["unix"])
        if cc_type == "msvc":
            pass
        elif cc_type == "unix":
            pass
        for ext in self.extensions:
            ext.extra_compile_args = compile_args
        for ext in self.extensions:
            ext.extra_link_args = link_args
        build_ext.build_extensions(self)

ext_modules = [Extension(name="crcc._platform.crc",
                         language="c",
                         sources=["src/crcc/crc.c",
                                  "src/crcc/crc_table.c",
                                  "src/crcc/crc_update.c",
                                  "src/crcc/crc_py.c"],
                         depends=["include/crcc/crc.h",
                                  "src/crcc/crc.def",
                                  "src/crcc/crc_defs.h",
                                  "src/crcc/crc_table.h",
                                  "src/crcc/crc_update.h"])]

setup(
    ext_modules = ext_modules,
    cmdclass = dict(build_ext=BuildExt),
)
