#!/usr/bin/env python3
"""
This is a script to assist with RV's package development in order to iterate and deploy easily
"""

__author__ = "Gabriela Roque Lopez"
__version__ = "0.1.0"
__license__ = "GPL-3.0"

import argparse


def get_package_info():
    """
    Looks up the Package name, Author and Version from the plugin PACKAGE file

    Returns:
        tuple (str, str, float): The name, author and latest version of this plugin

    """


def build():
    """
    Creates a 'build' folder and packages the script files into a zip .rvpkg file

    Returns:
        string: The packaged file location on disk as a string
    """
    return


def install(rvpkg_file_location):
    """
    Runs the 'rvpkg' program to add and install the current rvpkg file that it's inside the build folder
    It takes into account the current OS to find the correct folders

    Args:
        rvpkg_file_location (str): The location on disk of the rvpkg file to install

    Returns:

    """
    return


def clean_existing_installation():
    """
    Removes the contents of the 'build' folder
    """


def main(args):
    """ Main entry point of the app """
    print("hello world")
    print(args)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument("-b", "--build",
                        action="store_true",
                        default=True,
                        help="Creates the rvpkg file using the contents of the 'plugin' folder, defaults to True")

    parser.add_argument("-i", "--install",
                        action="store_true",
                        default=False,
                        help="Runs rvpkg -add and -install on the corresponding folder by operating system, "
                             "defaults to False")

    parser.add_argument("-t", "--test",
                        action="store_true",
                        default=False,
                        help="Run unit tests for plugin, defaults to False")

    parser.add_argument("-v", "--verbose",
                        action="count",
                        default=0,
                        help="Verbosity (-v, -vv, etc)")

    args = parser.parse_args()
    main(args)
