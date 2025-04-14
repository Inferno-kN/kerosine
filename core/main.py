from conservation import saveLoad
from gui import view
from core import gameplay
from player import player_info
import time



def start() -> None:
    view.output_info("greeting")
    # view.statusbar()
    save_info = saveLoad.load_all_data()
    menu(save_info)
    view.output_info("farewell")
    time.sleep(2)


def menu(data) -> None:
    view.output_info("menu")
    app = True
    result = None
    while app:
        selection_user = view.user_input()
        if selection_user.lower().replace(" ", "") == "новаяигра":
            player = player_info.create_player()
            result = gameplay.run_game(player)

            if result == "menu":
                view.output_info("menu")
                continue

            elif result == "exit":
                app = False
        
        elif selection_user.lower().replace(" ", "") == "загрузить":
            name = player_info.load_player(data)
            player = saveLoad.load_data_player(name)
            result = gameplay.run_game(player)
            
            if result == "menu":
                view.output_info("menu")
                continue

            elif result == "exit":
                app = False

        elif selection_user.lower() == "выход":
            app = False
        
        else:
            view.output_info("not_command")
        
        if result == "theend":
            saveLoad.del_data_player(player["name"])
            view.output_info("menu")


