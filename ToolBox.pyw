import os, sys, io
import re as regex

from PIL import Image
import PySimpleGUI as sGUI
from PySimpleGUI.PySimpleGUI import TIMEOUT_KEY

class PrintColors:
    HEADER = '\033[95m'
    BLUE = '\033[34m'
    LBLUE = '\033[94m'
    CYAN = '\033[36m'
    LCYAN = '\033[96m'
    GREEN = '\033[32m'
    LGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

window_size = (720, 480)
chara_baseSize = (100, 120)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./data/img")

    return os.path.join(base_path, relative_path)

def img_data(filepath, size=(100, 180)):
    """ Generate image data using PIL """
    img = Image.open(filepath)
    img.thumbnail(size)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()

def update_preview(window: sGUI.Window, source_index: int, dest_index: int, chara_list: list, remove_index: int = None):
    if (remove_index != None and source_index > dest_index):
        for i in range(remove_index, source_index, 1):
            chara_list[i] = chara_list[i + 1]
        chara_list[source_index] = None
        print(chara_list)

    for index in range(0, dest_index + 1, 1):
        chara_list[index] = "voyagerM.png" if chara_list[index] == None else chara_list[index]
        window[f"-CHARA{index}-{dest_index}"].update(image_data = img_data(resource_path(chara_list[index]), chara_baseSize))
        window[f"-CHARA{index}-{dest_index}"].metadata = chara_list[index]
    pass

if __name__ == "__main__" :
    img_path = resource_path("itto.png")
    #chara_size = (int(chara_baseSize * img.size[0] / img.size[1]), chara_baseSize)
    #print(img.size, img.size[0]/img.size[1], "|", chara_baseSize, "=>", chara_size, chara_size[0]/chara_size[1])

    max_chara = 45 + 1
    max_cols = int(window_size[0] / chara_baseSize[0])
    max_rows = int(max_chara / max_cols)
    print(max_cols, max_rows, max_cols * max_rows)

    preview0 = [
        [
            sGUI.Button("", image_data = img_data(resource_path("voyagerM.png"), chara_baseSize), image_size = chara_baseSize, border_width = (0, 0), key = f"-CHARA{0}-0", metadata = "voyagerM"),
            sGUI.Button("", image_data = img_data(resource_path("new.png"), chara_baseSize), image_size = chara_baseSize, border_width = (0, 0), key = f"-ADD-")
        ]
    ]
    preview1 = [
        [
            sGUI.Button("", image_data = None, image_size = chara_baseSize, border_width = (0, 0), key = f"-CHARA{0}-1", metadata = "voyagerM"),
            sGUI.Button("", image_data = None, image_size = chara_baseSize, border_width = (0, 0), key = f"-CHARA{1}-1", metadata = "albedo"),
            sGUI.Button("", image_data = img_data(resource_path("new.png"), chara_baseSize), image_size = chara_baseSize, border_width = (0, 0), key = f"-ADD-")
        ]
    ]
    preview2 = [
        [
            sGUI.Button("", image_data = None, image_size = chara_baseSize, border_width = (0, 0), key = f"-CHARA{0}-2", metadata = "voyagerM"),
            sGUI.Button("", image_data = None, image_size = chara_baseSize, border_width = (0, 0), key = f"-CHARA{1}-2", metadata = "albedo"),
            sGUI.Button("", image_data = None, image_size = chara_baseSize, border_width = (0, 0), key = f"-CHARA{2}-2", metadata = "itto"),
            sGUI.Button("", image_data = img_data(resource_path("new.png"), chara_baseSize), image_size = chara_baseSize, border_width = (0, 0), key = f"-ADD-")
        ]
    ]
    preview3 = [
        [
            sGUI.Button("", image_data = None, image_size = chara_baseSize, border_width = (0, 0), key = f"-CHARA{0}-3", metadata = "voyagerM"),
            sGUI.Button("", image_data = None, image_size = chara_baseSize, border_width = (0, 0), key = f"-CHARA{1}-3", metadata = "albedo"),
            sGUI.Button("", image_data = None, image_size = chara_baseSize, border_width = (0, 0), key = f"-CHARA{2}-3", metadata = "itto"),
            sGUI.Button("", image_data = None, image_size = chara_baseSize, border_width = (0, 0), key = f"-CHARA{3}-3", metadata = "zhongli"),
        ]
    ]
    preview = [preview0, preview1, preview2, preview3]

    #table =  [[sGUI.Button("", image_data = img_data(img_path, chara_baseSize), button_color=(sGUI.theme_background_color(), sGUI.theme_background_color()), border_width=0, key=(row,col)) for col in range(max_cols)] for row in range(max_rows)]
    table = sGUI.Column([[sGUI.Button("", image_data = img_data(img_path, chara_baseSize), image_size = chara_baseSize, border_width = (0, 0), key=(row,col)) for col in range(max_cols)] for row in range(max_rows)], justification = "center")
    table = []
    for row in range(max_rows):
        line = []
        for col in range(max_cols):
            line.append(sGUI.Button("", image_data = img_data(img_path, chara_baseSize), image_size = chara_baseSize, border_width = (0, 0), key=(row,col)))
            line.append(sGUI.Stretch())
        line.pop(-1)
        table.append(line)
        table.append([sGUI.VStretch()])
    table.pop(-1)

    #table = [
    #    [sGUI.Button("0|0"), sGUI.Stretch(), sGUI.Button("0|1"), sGUI.Stretch(), sGUI.Button("0|2")],
    #    [sGUI.VStretch()],
    #    [sGUI.Button("1|0"), sGUI.Stretch(), sGUI.Button("1|1"), sGUI.Stretch(), sGUI.Button("1|2")],
    #    [sGUI.VStretch()],
    #    [sGUI.Button("2|0"), sGUI.Stretch(), sGUI.Button("2|1"), sGUI.Stretch(), sGUI.Button("2|2")]
    #]

    layout = [
        [sGUI.Text("Button Grid")],
        [sGUI.Column(preview0, visible = True, justification = "center", key = "COL0"), sGUI.Column(preview1, visible = False, justification = "center", key = "COL1"), sGUI.Column(preview2, visible = False, justification = "center", key = "COL2"), sGUI.Column(preview3, visible = False, justification = "center", key = "COL3")],
       # [sGUI.Frame("", layout = table, pad = (0, 0), expand_x = True, expand_y = True)]
    ]

    # Resource window icon
    if (sys.platform.startswith("win")):
        window_icon = resource_path("icon.ico")
    else:
        window_icon = resource_path("icon.png")

    # Create main Window
    window = sGUI.Window("Genshin Impact ToolBox", layout, icon = window_icon, titlebar_icon = window_icon, size = window_size, margins = (0, 0), element_padding = (0, 0), use_ttk_buttons = True, resizable = True, finalize = True)
    
    # Bind overing event for character preview
    [[window[f"-CHARA{index}-{preview_index}"].bind("<Enter>", "+OVER+") for preview_index in range(index, len(preview))] for index in range(len(preview))]

    preview_chara_list = ["voyagerM.png", "albedo.png", "itto.png", "zhongli.png"]
    preview_index = 0
    add_pattern = "^-ADD-"
    chara_pattern = "^-CHARA\d-\d$"
    over_pattern = ".*[+]OVER[+]"
    # Create an event loop
    while True:
        event, values = window.read()

        print(event, values)
        # End program if user closes window or presses the OK button
        if (event == sGUI.WIN_CLOSED):
            break
        elif (regex.match(add_pattern, event)):
            window[f"COL{preview_index}"].update(visible = False)
            update_preview(window = window, source_index = preview_index, dest_index = preview_index + 1, chara_list = preview_chara_list)
            preview_index += 1
            window[f"COL{preview_index}"].update(visible = True)
        elif (regex.match(chara_pattern, event)):
            chara_id = window[event].metadata
            print(chara_id)
            print(window[event].get_size())
            index = int(regex.findall("\d", event)[0])
            if (preview_index > 0):
                window[f"COL{preview_index}"].update(visible = False)
                update_preview(window = window, source_index = preview_index, dest_index = preview_index - 1, remove_index = index, chara_list = preview_chara_list)
                preview_index -= 1
                window[f"COL{preview_index}"].update(visible = True)
        elif (regex.match(over_pattern, event)):
            index = int(regex.findall("\d", event)[0])
            print(f"{PrintColors.FAIL}ToDo: Update display stats{PrintColors.ENDC}")
        elif (event == TIMEOUT_KEY):
            pass

    window.close()