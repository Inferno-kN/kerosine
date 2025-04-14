from gui import view
from conservation.saveLoad import save, load_data_player
from items import items_info


def load_player(data_player):
    view.output_profile(data_player)
    view.output_info("select_profile")
    return view.user_input()



def create_player():
    view.output_stage("input_name")
    name = view.user_input()
    user = {
        "name" : name,
        "health" : 100,
        "destroyed_cars" : 0,
        "inventory" : {"bottle" : [items_info.items_bootle["bootle_kerosine_small"]],
                       "lighter": [items_info.items_light["lighter_small"]]},
        "live" : 1,
        "difficulty" : "easy",
        "new" : True
    }

    save(user)

    return user
