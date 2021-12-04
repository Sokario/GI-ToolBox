import os
import sys

import PySimpleGUI as sGUI

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./data/img")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__" :
    itto_img = resource_path("itto.png")
    image_viewer = [
        [sGUI.Text("Choose an image from list on left:")],
        [sGUI.Text(size = (40, 1), key = "-TOUT-")],
        [sGUI.Image(filename = itto_img, key = "-IMAGE-")]
    ]
    layout = [[sGUI.Text("ToolBox from PySimpleGUI")], [sGUI.Button("OK")], image_viewer]

    # Create the window
    window = sGUI.Window("Genshin Impact ToolBox", layout, margins = (720, 480)).read()

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sGUI.WIN_CLOSED:
            break

    window.close()