from ctypes import alignment
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
chara_size = (100, 120)
party_Size = (380, 100)
background_color = "#3e4557"
text_color = "#e5d6b6"
full_preview_list = [character_list[i]() for i in range(len(character_list)) if (character_list[i] != BaseCharacter and character_list[i] != Voyager)]
full_preview_list.append(Voyager())
chara_preview_list = [len(full_preview_list)-1, None, None, None]
popup = None

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./data/img")

    return os.path.join(base_path, relative_path)

def img_data(filepath, size = None):
    """ Generate image data using PIL """
    # !!!! Itto casse les couille sur la taille d'image
    img = Image.open(filepath)
    if (size != None):
        img.thumbnail(size)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()

def update_information(window: sGUI.Window, chara_index: int):
    window["CHARA NAME"].update(full_preview_list[chara_preview_list[chara_index]].name)
    window["PARTY IMAGE"].update(data = img_data(resource_path(full_preview_list[chara_preview_list[chara_index]].pictures["banner"]), party_Size))

def update_preview(window: sGUI.Window, source_index: int, dest_index: int, remove_index: int = None):
    if (remove_index != None and source_index > dest_index):
        for i in range(remove_index, source_index, 1):
            chara_preview_list[i] = chara_preview_list[i + 1]
        chara_preview_list[source_index] = None
        print(chara_preview_list)

    for index in range(0, dest_index + 1, 1):
        chara_preview_list[index] = -1 if chara_preview_list[index] == None else chara_preview_list[index]
        window[f"-CHARA{index}-{dest_index}"].update(image_data = img_data(resource_path(full_preview_list[chara_preview_list[index]].pictures["portrait"]), chara_size))
    
    print(chara_preview_list)

def choose_chara_popup(preview_index: int):
    max_cols = 5
    table = []
    line = []
    if (preview_index != 0):
        line.append(sGUI.Button("", image_data = img_data(resource_path("delete.png"), chara_size), button_color = (sGUI.theme_background_color(), sGUI.theme_background_color()), border_width = 0, key = f"-DELETE-"))
    for index in range(len(full_preview_list)):
        if (len(line) % max_cols <= 0):
            if (len(line) != 0):
                table.append(line)
            line = []
        line.append(sGUI.Button("", image_data = img_data(resource_path(full_preview_list[index].pictures["portrait"]), chara_size), button_color = (sGUI.theme_background_color(), sGUI.theme_background_color()), border_width = 0, disabled = True if index in chara_preview_list else False, key = f"-CHOICE-{index}"))
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

    preview0 = [
        [
            sGUI.Button("", image_data = img_data(resource_path("voyager.png"), chara_size), image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{0}-0"),
            sGUI.Button("", image_data = img_data(resource_path("new.png"), chara_size), image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{1}-")
        ]
    ]
    preview1 = [
        [
            sGUI.Button("", image_data = None, image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{0}-1"),
            sGUI.Button("", image_data = None, image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{1}-1"),
            sGUI.Button("", image_data = img_data(resource_path("new.png"), chara_size), image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{2}-")
        ]
    ]
    preview2 = [
        [
            sGUI.Button("", image_data = None, image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{0}-2"),
            sGUI.Button("", image_data = None, image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{1}-2"),
            sGUI.Button("", image_data = None, image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{2}-2"),
            sGUI.Button("", image_data = img_data(resource_path("new.png"), chara_size), image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{3}-")
        ]
    ]
    preview3 = [
        [
            sGUI.Button("", image_data = None, image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{0}-3"),
            sGUI.Button("", image_data = None, image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{1}-3"),
            sGUI.Button("", image_data = None, image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{2}-3"),
            sGUI.Button("", image_data = None, image_size = chara_size, border_width = (0, 0), button_color = background_color, key = f"-CHARA{3}-3"),
        ]
    ]
    preview = [preview0, preview1, preview2, preview3]

    layout = [
        [sGUI.Text("Button Grid", background_color = background_color)],
        [sGUI.Column(preview0, visible = True, justification = "center", key = "COL0"), sGUI.Column(preview1, visible = False, justification = "center", key = "COL1"), sGUI.Column(preview2, visible = False, justification = "center", key = "COL2"), sGUI.Column(preview3, visible = False, justification = "center", key = "COL3")],
        [sGUI.HSeparator()],
        [sGUI.Text("CHARACTER NAME", font = ('Arial', 16, 'bold'), background_color = background_color, text_color = text_color, pad = (20, 0, 0, 0), key = "CHARA NAME"), sGUI.Stretch(background_color = background_color), sGUI.Image(data = img_data(resource_path("voyager_party.png"), party_Size), background_color = background_color, key = "PARTY IMAGE")],
        [sGUI.HSeparator()]
    ]

    # Resource window icon
    if (sys.platform.startswith("win")):
        window_icon = resource_path("icon.ico")
    else:
        window_icon = resource_path("icon.png")

    # Create main Window
    window = sGUI.Window("Genshin Impact ToolBox", layout, icon = window_icon, titlebar_icon = window_icon, size = window_size, margins = (0, 0), element_padding = (0, 0), use_ttk_buttons = True, background_color = background_color, resizable = True, finalize = True)
    
    # Bind overing event for character preview
    [[window[f"-CHARA{index}-{preview_index}"].bind("<Enter>", "+OVER+") for preview_index in range(index, len(preview))] for index in range(len(preview))]

    preview_index = 0
    chara_index = None
    chara_add = False
    add_pattern = "^-ADD-"
    chara_pattern = "^-CHARA\d-"
    change_pattern = "^-CHANGE-"
    delete_pattern = "^-DELETE-"
    over_pattern = ".*[+]OVER[+]"
    # Create an event loop
    while True:
        event, values = window.read(100)

        #print(f"WINDOW => {event}: {values}")
        # End program if user closes window or presses the OK button
        if (event == sGUI.WIN_CLOSED):
            break
        elif (regex.match(over_pattern, event)):
            index = int(regex.findall("\d", event)[0])
            update_information(window, index)
            print(f"{PrintColors.FAIL}ToDo: Update display stats -------- !!!!! Nedd to be stop while popup is open{PrintColors.ENDC}")
        elif (regex.match(chara_pattern, event)):
            chara_index = regex.findall("\d", event)
            chara_add = len(chara_index) == 1
            chara_index = int(chara_index[0])
            popup = choose_chara_popup(preview_index + (1 if chara_add else 0))
        elif (regex.match(change_pattern, event)):
            chara_preview_list[chara_index] = values[event]
            update_preview(window = window, source_index = preview_index, dest_index = preview_index)
            update_information(window, chara_index)
        elif (regex.match(add_pattern, event)):
            chara_preview_list[chara_index] = values[event]
            window[f"COL{preview_index}"].update(visible = False)
            update_preview(window = window, source_index = preview_index, dest_index = preview_index + 1)
            preview_index += 1
            window[f"COL{preview_index}"].update(visible = True)
            update_information(window, chara_index)
        elif (regex.match(delete_pattern, event)):
            window[f"COL{preview_index}"].update(visible = False)
            update_preview(window = window, source_index = preview_index, dest_index = preview_index - 1, remove_index = chara_index)
            preview_index -= 1
            window[f"COL{preview_index}"].update(visible = True)
            update_information(window, 0)
        elif (event == TIMEOUT_KEY):
            if (popup != None):
                popup_event, popup_values = popup.read(100)

                #print(f"POPUP => {popup_event}: {popup_values}")
                choice_pattern = "^-CHOICE-"
                if (popup_event == "-EXIT-"):
                    popup.close()
                    popup = None
                elif (regex.match(choice_pattern, popup_event)):
                    index = int(regex.findall("\d", popup_event)[0])
                    window.write_event_value("-ADD-" if chara_add else "-CHANGE-", index)
                    popup.close()
                    popup = None
                elif (regex.match(delete_pattern, popup_event)):
                    if (not chara_add): window.write_event_value("-DELETE-", None)
                    popup.close()
                    popup = None
                else:
                    pass

    window.close()