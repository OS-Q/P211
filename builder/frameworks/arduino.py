"""
Arduino

Arduino Wiring-based Framework allows writing cross-platform software to
control devices attached to a wide range of Arduino boards to create all
kinds of creative coding, interactive objects, spaces or physical experiences.

http://www.stm32duino.com
"""

import sys
from os.path import join, isfile

from SCons.Script import DefaultEnvironment, SConscript

env = DefaultEnvironment()
mcu = env.BoardConfig().get("build.mcu")
core = env.BoardConfig().get("build.core", "")


if core == "maple":
    build_script = join(
        env.PioPlatform().get_package_dir("framework-N3"),
        "tools", "platformio-build-%s.py" % mcu[0:7])
    if isfile(build_script):
        SConscript(build_script)
    else:
        sys.stderr.write(
            "Error: %s family is not supported by maple core\n" % mcu[0:7])
        env.Exit(1)

else:
    SConscript(
        join(env.PioPlatform().get_package_dir(
            "framework-N5"),
            "tools", "platformio-build.py"))
