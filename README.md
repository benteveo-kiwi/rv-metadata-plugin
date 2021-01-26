# RV Shotgun plugin to copy metadata
This is a plugin that allows the user to copy certain metadata from an image in RV.
[RV](https://www.shotgunsoftware.com/rv) is an image, audio and video review software owned by Shotgun.

### Usage

The plugin finds information in the image metadata for a contact-sheet in which each quadrant corresponds to a location 
on disk where the original is stored.

It was written to help a client with a particular need. Given a contact-sheet with different clips rendered as JPEG 
sequence, the metadata contains a list of the locations of the original clips on disk
as well as the coordinates in pixels of each clip on the image. The plugin takes the location
of the mouse pointer and matches it to the location on disk copying to the clipboard.

#### Requirements

* RV-2021.0.0

### Installation

1. Clone repo
2. Zip and install plugin:
    * Using the `build-tool` (currently only works on Windows):
    ```bash
    python3 build-tool.py --install
    ```
3. Open RV
4. Open contact sheet sequence
5. Middle mouse click in the desired part of the clip to copy location to 

#### Tools used and compatible versions

* Written in Python 3
* Tested with RV-2021.0.0
* Uses Pyside2 to copy the data to the clipboard
* Plugin runs in Windows, Mac and Linux


----------------------------------------------------------------------------
_Copyright 2020 Benteveo Ltd._

_Licensed under the GNU General Public License v3.0_