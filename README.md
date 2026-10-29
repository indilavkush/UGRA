UGRA

UGRA is an experimental, open-source, community-driven AI platform.
hey myself lavkush
great welcome to all
Our goal is to build a modular platform where developers can contribute skills, tools, tests, and new capabilities.

Current Features

- Automatic skill discovery
- Modular Python skill system
- Skill descriptions
- Automatic skill tests
- Basic calculator
- System information
- Greeting and project information skills

Project Structure

UGRA/
├── main.py
├── README.md
└── skills/
    ├── __init__.py
    ├── hello.py
    ├── about.py
    ├── calculator.py
    └── system_info.py

Requirements

- Python 2.7 for the current prototype
- PyCharm or another Python editor

Python 2.7 is obsolete and unsupported. A supported Python version is planned for future development before production use.

Running UGRA

Run "main.py" from your Python editor.

Choose an available skill from the menu and follow its instructions.

Creating a Skill

Every skill should provide:

- "NAME": A readable skill name
- "DESCRIPTION": A short explanation
- "run(text)": The function that performs the skill's task
- "test()": A basic automated test

Example:

NAME = "Example"
DESCRIPTION = "An example skill."


def run(text):
    return "You entered: " + text


def test():
    assert run("Hello") == "You entered: Hello"
    return True

Save a new skill as a Python file inside the "skills" directory.

The current prototype discovers Python files in that directory and loads modules that provide a "run()" function.

Project Direction

Planned development areas:

1. Migrate to a supported Python version.
2. Improve skill validation and error handling.
3. Add permission controls for sensitive operations.
4. Integrate an AI model.
5. Build developer documentation and automated testing.
6. Welcome community contributions.

Open Source

UGRA is an evolving experiment. Features, architecture, and project goals may change as development and community feedback progress.