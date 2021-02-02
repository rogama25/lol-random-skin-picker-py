import logging
import time

from lcu_driver import Connector
from lcu_driver.utils import return_process

import os
import easygui
import requests

version = None


def wait_for_league():
    process = None
    while not process:
        process = return_process(['LeagueClientUx.exe', 'LeagueClientUx'])
        time.sleep(2)
    return process


logger = logging.getLogger("rogama-utils")


class MyConnector(Connector):
    def start(self) -> None:
        """Starts the connector. This method should be overridden if different behavior is required.
    
        :rtype: None
        """
        try:
            def wrapper():
                connection = wait_for_league()
                self.create_connection(connection)
                self.loop.run_until_complete(self.connection.init())
                
                if self._repeat_flag and len(self.ws.registered_uris) > 0:
                    logger.debug('Repeat flag=True. Looking for new clients.')
                    wrapper()
            
            wrapper()
        except KeyboardInterrupt:
            logger.info('Event loop interrupted by keyboard')
            

def my_exit(icon, item=None):
    icon.visible = False
    icon.update_menu()
    icon.stop()
    os._exit(0)
    

def about():
    easygui.msgbox("""Program created by rogama25. This is free and open source, avaliable on
https://github.com/rogama25/lol-random-skin-picker-py.

Version 0.2""",
                   "LoL random skin selector")

def get_skin_name(selected, skin_names, skin_ids):
    if os.path.exists("./english"):
        global version
        champ_name = str(skin_names[0])
        if champ_name == "Wukong":
            champ_name = "MonkeyKing"
        if version is None:
            print("Downloading versions...")
            versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
            version = str(versions[0])
        print("Getting data for", champ_name)
        champ_info = requests.get("http://ddragon.leagueoflegends.com/cdn/" + version +
        "/data/en_US/champion/" + champ_name + ".json").json()
        for skin in champ_info["data"][champ_name]["skins"]:
            if skin["id"] == str(selected):
                if skin["name"] == "default":
                    return champ_name
                return skin["name"]
    return skin_names[skin_ids.index(selected)]
