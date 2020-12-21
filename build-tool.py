#!/usr/bin/env python3
"""
This is a script to assist with RV's package development in order to iterate and deploy easily
"""

__author__ = "Gabriela Roque Lopez"
__version__ = "0.1.0"
__license__ = "GPL-3.0"

import argparse
import os
import platform
import subprocess
import zipfile


# Location of the rvpkg app on different platforms
MACOS_RVPKG = "/Applications/RV.app/Contents/MacOS/rvpkg"
WINDOWS_RVPKG = "C:\\Program Files\\Shotgun\\RV-2021.0.0\\bin\\rvpkg.exe"
LINUX_RVPKG = "rvpkg"

# Location of the installation directory on different platforms
MACOS_PATH_TO_AREA = "~/Library/Application\ Support/RV"
# TODO: get the home directory with python?
WINDOWS_PATH_TO_AREA = "C:\\Users\\Gabita\\AppData\\Roaming\\RV"
LINUX_PATH_TO_AREA = "~/.rv/"

# Name of the package hardcoded for now
PACKAGE_NAME = "Metadata Finder"

PLATFORM_NAME = platform.system()


def get_package_info():
    """
    Looks up the Package name and Version from the plugin PACKAGE file

    Returns:
        tuple (str, float): The name and latest version of this plugin

    """


def write_rvpkg_file(path, rvpkg_file):
    """
    It grabs all the files inside the path folder and adds them to the zip rvpkg file

    Args:
        path: Folder where the plugin files are stored
        rvpkg_file: ZipFile instance of the rvpkg file
    """

    for root, dirs, files in os.walk(path):
        for file in files:
            rvpkg_file.write(filename=os.path.join(root, file), arcname=file)


def build():
    """
    Creates a 'build' folder and packages the script files into a zip .rvpkg file

    Returns:
        string: The packaged file location on disk as a string
    """
    try:
        os.mkdir("build")
    except FileExistsError:
        print("Build folder already exists")

    rvpkg_file_path = "build\\metadata_finder-0.1.rvpkg"

    with zipfile.ZipFile(rvpkg_file_path, mode='w') as rvpkg_file:
        write_rvpkg_file("plugin", rvpkg_file)

    return rvpkg_file_path


def install(rvpkg_file_path):
    """
    Runs the 'rvpkg' program to add and install the current rvpkg file that it's inside the build folder
    It takes into account the current OS to find the correct folders

    Args:
        rvpkg_file_path (str): The location on disk of the rvpkg file to install
    """
    clean_existing_installation()

    process = subprocess.run([WINDOWS_RVPKG, "-install", "-add", WINDOWS_PATH_TO_AREA, rvpkg_file_path],
                            capture_output=True)

    print(process)


def clean_existing_installation():
    """
    Uninstalls the plugin from RV
    """
    subprocess.run([WINDOWS_RVPKG, "-remove", "-force", PACKAGE_NAME])


def restart_rv():
    """
    Kills all current instances of RV and starts a new one
    """
    # TODO: Implement other for other platforms
    if PLATFORM_NAME == "Windows":
        subprocess.run(["taskkill", "/F", "/IM", "rv.exe", "/T"])
        subprocess.run(["start", "RV"], shell=True)
        print("Signal sent to start RV")

    if PLATFORM_NAME == "Linux":
        print("Restart on Linux not implemented yet")

    if PLATFORM_NAME == "Darwin":
        print("Restart on MacOS not implemented yet")


def main(args):
    """ Main entry point of the app """

    if args.build:
        rvpkg_file_path = build()

    if args.install:
        install(rvpkg_file_path)

    if args.restart:
        print("Restarting current open RV session")
        restart_rv()


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

    parser.add_argument("-r", "--restart",
                        action="store_true",
                        default=False,
                        help="Restarts the current open instance of RV in order to get the latest plugin changes"
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
