import pystray
from PIL import Image
import league
from utils import my_exit

icon = pystray.Icon("LoL skin randomizer")
icon.icon = Image.open("icon.png")
icon.title = "LoL skin randomizer"

item = pystray.MenuItem("Please start LoL", action=league.randomize, enabled=False, default=True)
exit_button = pystray.MenuItem("Exit", action=my_exit)
menu = pystray.Menu(item, exit_button)
league.set_items(item, icon)
icon.menu = menu

icon.run(league.start)
