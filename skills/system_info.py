# -*- coding: utf-8 -*-

import platform
import sys

NAME = "System Information"
DESCRIPTION = "Shows basic computer and Python information."


def run(text):
    command = text.strip().lower()

    if command == "os":
        return platform.platform()

    elif command == "python":
        return sys.version.split()[0]

    elif command == "machine":
        return platform.machine()

    elif command == "all":
        info = []
        info.append("Operating System: " + platform.platform())
        info.append("Python Version: " + sys.version.split()[0])
        info.append("Architecture: " + platform.machine())
        return "\n".join(info)

    else:
        return "Commands: os, python, machine, all"


def test():
    assert len(run("os")) > 0
    assert len(run("python")) > 0
    assert len(run("machine")) > 0
    assert "Operating System:" in run("all")
    return True
