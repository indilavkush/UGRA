# -*- coding: utf-8 -*-

NAME = "About UGRA"
DESCRIPTION = "Shows information about the UGRA project."


def run(text):
    return "UGRA is an open-source AI platform built for community contributions."


def test():
    result = run("info")
    assert "open-source AI platform" in result
    return True
