# -*- coding: utf-8 -*-

import os
import importlib


def load_skills():
    loaded = []
    folder = os.path.join(os.path.dirname(__file__), "skills")

    for filename in sorted(os.listdir(folder)):
        if filename.endswith(".py") and filename != "__init__.py":
            name = filename[:-3]

            try:
                module = importlib.import_module("skills." + name)

                if hasattr(module, "run"):
                    loaded.append((name, module))

            except Exception as error:
                print("Skill loading error:", name, error)

    return loaded


def test_skills(skills):
    print("\nUGRA SKILL TESTS")
    print("-" * 30)

    for name, module in skills:
        if hasattr(module, "test"):
            try:
                result = module.test()

                if result:
                    print(name, "- PASSED")
                else:
                    print(name, "- FAILED")

            except Exception as error:
                print(name, "- FAILED:", error)
        else:
            print(name, "- NO TEST AVAILABLE")


def main():
    print("=" * 35)
    print("UGRA OPEN AI PLATFORM")
    print("=" * 35)

    skills = load_skills()

    if not skills:
        print("No skills available.")
        return

    test_skills(skills)

    print("\nAVAILABLE SKILLS")
    print("-" * 35)

    for number, item in enumerate(skills, 1):
        name, module = item
        title = getattr(module, "NAME", name)
        description = getattr(module, "DESCRIPTION", "No description")

        print(str(number) + ". " + title)
        print("   " + description)

    print("\n0. Exit")

    choice = raw_input("\nChoose a skill number: ")

    try:
        index = int(choice)

        if index == 0:
            print("UGRA closed.")
            return

        if index < 1 or index > len(skills):
            print("Invalid option.")
            return

        name, module = skills[index - 1]
        message = raw_input("Enter your message: ")

        print("\nUGRA:", module.run(message))

    except ValueError:
        print("Please enter a number.")


if __name__ == "__main__":
    main()