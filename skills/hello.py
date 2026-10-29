# -*- coding: utf-8 -*-

NAME = "Greeting"
DESCRIPTION = "Greets the user and responds to messages."


def run(text):
    return "UGRA received: " + text


def test():
    result = run("Hello")
    assert result == "UGRA received: Hello"
    return True