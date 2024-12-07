"""renpy
init python:
"""

import urllib.request
import os

downloads_dir = "game/GiftForYou=)"

def download_file(url, save_path):
    global downloads_dir
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)
    try:
        urllib.request.urlretrieve(url, save_path)
    except Exception as e:
        renpy.say("System", f"Error Downloading file: {e}")
