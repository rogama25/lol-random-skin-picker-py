import time
import logging
from lcu_driver.connection import Connection
import threading
from utils import MyConnector, my_exit
import random
import easygui

logger = logging.getLogger("lol-autolockin")
connector = MyConnector()
choose_new = False
menu_item = None
icon = None


def randomize():
    global choose_new
    if menu_item.text == "Randomize":
        choose_new = True
    

def set_items(item, menu):
    global menu_item, icon
    menu_item = item
    icon = menu


def start(icon):
    icon.visible = True
    t = threading.Thread(target=connector.start)
    t.start()


@connector.ready
async def connect(connection: Connection):
    global choose_new
    print("Connected to LCU API")
    while True:
        try:
            req_type = "/lol-champ-select/v1/session"
            req = await connection.request("get", req_type)
            data = await req.json()
            if "errorCode" in data:
                menu_item._text = menu_item._wrap("Not in champ select")
                menu_item._enabled = menu_item._wrap(False)
                icon.update_menu()
                time.sleep(5)
                continue
            req_type = "/lol-champ-select/v1/skin-selector-info"
            req = await connection.request("get", req_type)
            data = await req.json()
            if data["selectedChampionId"] == 0:
                menu_item._text = menu_item._wrap("No champ selected")
                menu_item._enabled = menu_item._wrap(False)
                icon.update_menu()
                time.sleep(2)
                continue
            menu_item._text = menu_item._wrap("Randomize")
            menu_item._enabled = menu_item._wrap(True)
            icon.update_menu()
            if choose_new:
                choose_new = False
                list_skins = []
                skin_names = []
                req_type = "/lol-champ-select/v1/skin-carousel-skins"
                req = await connection.request("get", req_type)
                data = await req.json()
                for skin in data:
                    if skin["unlocked"] and not skin["disabled"]:
                        list_skins.append(skin["id"])
                        skin_names.append(skin["name"])
                selected = random.choice(list_skins)
                pos = list_skins.index(selected)
                req_type = "/lol-champ-select/v1/session/my-selection"
                req_data = {"selectedSkinId": selected}
                req = await connection.request("patch", req_type, data=req_data)
                data = await req.json()
                print("Available", list_skins, skin_names, "Chosen", selected)
                easygui.msgbox("Skin selected: " + str(skin_names[pos]), "LoL random skin selector")
            time.sleep(1)
        except:
            my_exit(icon)


@connector.close
async def disconnect(_):
    print("Disconnected from League, exiting...")
