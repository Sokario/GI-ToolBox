import os
import sys
import io

from PIL import Image, ImageTk
import PySimpleGUI as sGUI
from PySimpleGUI.PySimpleGUI import TIMEOUT_KEY

window_size = (720, 480)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./data/img")

    return os.path.join(base_path, relative_path)

def img_data(filepath, size=(100, 180)):
    """
    Generate image data using PIL
    """
    img = Image.open(filepath)
    img.thumbnail(size)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()

if __name__ == "__main__" :
    img_path = resource_path("itto.png")
    chara_baseSize = (80, 100)
    #chara_size = (int(chara_baseSize * img.size[0] / img.size[1]), chara_baseSize)
    #print(img.size, img.size[0]/img.size[1], "|", chara_baseSize, "=>", chara_size, chara_size[0]/chara_size[1])
    
    #layout =   [[sg.Text('Button Grid', font='Default 25')],
    #           [sg.Text(size=(15,1), key='-MESSAGE-', font='Default 20')]]

    max_preview = 45 + 1
    max_cols = int(window_size[0] / chara_baseSize[0])
    max_rows = int(max_preview / max_cols)
    print(max_cols, max_rows, max_cols * max_rows)
    layout = [
        [sGUI.Text("Button Grid")],
        [sGUI.Button("", image_data = img_data(img_path, chara_baseSize), button_color=(sGUI.theme_background_color(), sGUI.theme_background_color()), border_width = 0, key = "EXIT")]
        ]
    table =  [[sGUI.Button("", image_data = img_data(img_path, chara_baseSize), button_color=(sGUI.theme_background_color(), sGUI.theme_background_color()), border_width=0, key=(row,col)) for col in range(max_cols)] for row in range(max_rows)]

    layout += table#[[sGUI.Table(table)]]

    chara_num = 45 + 1

    # Resource window icon
    if (sys.platform.startswith("win")):
        window_icon = resource_path("icon.ico")
    else:
        window_icon = resource_path("icon.png")

    # Create main Window
    window = sGUI.Window("Genshin Impact ToolBox", layout, icon = window_icon, titlebar_icon = window_icon, size = window_size, resizable = True, finalize = True)   

    # Create an event loop
    while True:
        event, values = window.read(timeout = 100)

        print(event)        
        # End program if user closes window or presses the OK button
        if (event == "EXIT" or event == sGUI.WIN_CLOSED):
            break
        elif (event == TIMEOUT_KEY):
            #LayoutUpdate(window, chara_baseSize)
            #ImageUpdate(window, img_path, chara_baseSize)
            pass

    window.close()