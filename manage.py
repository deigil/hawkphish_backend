#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import pip

def install_packages():
    """Install packages listed in requirements.txt using pip."""
    try:
        with open('requirements.txt') as f:
            packages = [line.strip() for line in f if line.strip()]
        if packages:
            for package in packages:
                pip.main(["install", package])
            print("All required packages installed successfully!")
        else:
            print("No packages found in requirements.txt.")
    except Exception as e:
        print(f"Failed to install packages: {e}")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobackend.settings')

    # Check for required packages before executing any other command
    install_packages()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
