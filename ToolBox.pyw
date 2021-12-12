import os, sys, io
import re as regex

from PIL import Image
import PySimpleGUI as sGUI
from PySimpleGUI.PySimpleGUI import TIMEOUT_KEY

from src.characters import *
from src.characters.characterClass import BaseCharacter
from src.characters.voyager import Voyager

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
chara_preview_list = [None, None, None, None]
full_preview_list = [character_list[i]() for i in range(len(character_list)) if (character_list[i] != BaseCharacter and character_list[i] != Voyager)]
full_preview_list.append(Voyager())
popup = None

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

def update_preview(window: sGUI.Window, source_index: int, dest_index: int, remove_index: int = None):
    if (remove_index != None and source_index > dest_index):
        for i in range(remove_index, source_index, 1):
            chara_preview_list[i] = chara_preview_list[i + 1]
        chara_preview_list[source_index] = None
        print(chara_preview_list)

    for index in range(0, dest_index + 1, 1):
        chara_preview_list[index] = -1 if chara_preview_list[index] == None else chara_preview_list[index]
        window[f"-CHARA{index}-{dest_index}"].update(image_data = img_data(resource_path(full_preview_list[chara_preview_list[index]].pictures["portrait"]), chara_baseSize))
        window[f"-CHARA{index}-{dest_index}"].metadata = chara_preview_list[index]
    
    print(chara_preview_list)

def choose_chara_popup(preview_index: int):
    max_cols = 5
    table = []
    line = []
    if (preview_index != 0):
        line.append(sGUI.Button("", image_data = img_data(resource_path("delete.png"), chara_baseSize), button_color = (sGUI.theme_background_color(), sGUI.theme_background_color()), border_width = 0, key = f"-DELETE-"))
    for index in range(len(full_preview_list)):
        if (len(line) % max_cols <= 0):
            if (len(line) != 0):
                table.append(line)
            line = []
        line.append(sGUI.Button("", image_data = img_data(resource_path(full_preview_list[index].pictures["portrait"]), chara_baseSize), button_color = (sGUI.theme_background_color(), sGUI.theme_background_color()), border_width = 0, metadata = index, key = f"-CHOICE-{index}"))
    table.append(line)

    popup_layout = [
        [sGUI.Text("Choose a character")],
        table,
        [sGUI.HSeparator()]
    ]

    popup = sGUI.Window("Character available", popup_layout, no_titlebar = True, grab_anywhere = False, grab_anywhere_using_control = False, keep_on_top = True, finalize = True)
    popup.bind("<FocusOut>", "-EXIT-")

    return popup

if __name__ == "__main__" :
    print(full_preview_list[0].pictures["portrait"])
    #chara_size = (int(chara_baseSize * img.size[0] / img.size[1]), chara_baseSize)
    #print(img.size, img.size[0]/img.size[1], "|", chara_baseSize, "=>", chara_size, chara_size[0]/chara_size[1])

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

    preview_index = 0
    chara_index = None
    add_pattern = "^-ADD-"
    chara_pattern = "^-CHARA\d-\d$"
    change_pattern = "^-CHANGE-"
    delete_pattern = "^-DELETE-"
    over_pattern = ".*[+]OVER[+]"
    # Create an event loop
    while True:
        event, values = window.read(100)

        print(f"WINDOW => {event}: {values}")
        # End program if user closes window or presses the OK button
        if (event == sGUI.WIN_CLOSED):
            break
        elif (regex.match(over_pattern, event)):
            index = int(regex.findall("\d", event)[0])
            print(f"{PrintColors.FAIL}ToDo: Update display stats -------- !!!!! Nedd to be stop while popup is open{PrintColors.ENDC}")
        elif (regex.match(chara_pattern, event)):
            chara_index = int(regex.findall("\d", event)[0])
            popup = choose_chara_popup(preview_index)
        elif (regex.match(change_pattern, event)):
            chara_preview_list[chara_index] = values[event]
            update_preview(window = window, source_index = preview_index, dest_index = preview_index)
        elif (regex.match(delete_pattern, event)):
            window[f"COL{preview_index}"].update(visible = False)
            update_preview(window = window, source_index = preview_index, dest_index = preview_index - 1, remove_index = chara_index)
            preview_index -= 1
            window[f"COL{preview_index}"].update(visible = True)
        elif (regex.match(add_pattern, event)):
            window[f"COL{preview_index}"].update(visible = False)
            update_preview(window = window, source_index = preview_index, dest_index = preview_index + 1)
            preview_index += 1
            window[f"COL{preview_index}"].update(visible = True)
        elif (event == TIMEOUT_KEY):
            if (popup != None):
                popup_event, popup_values = popup.read(0)

                #print(f"POPUP => {popup_event}: {popup_values}")
                choice_pattern = "^-CHOICE-"
                if (popup_event == "-EXIT-"):
                    popup.close()
                    popup = None
                elif (regex.match(choice_pattern, popup_event)):
                    window.write_event_value("-CHANGE-", popup[popup_event].metadata)
                    popup.close()
                    popup = None
                elif (regex.match(delete_pattern, popup_event)):
                    window.write_event_value("-DELETE-", None)
                    popup.close()
                    popup = None
                else:
                    pass

    window.close()