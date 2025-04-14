import json
import os


def load_all_data() -> list:
    path = os.environ.get("LOCALAPPDATA") + "\\Kerosine"

    if not os.path.exists(path):
        return []
    
    lst_profile = os.listdir(path)

    data_lst = []
    for name in lst_profile:
        name = name.replace(".json", "")
        data_lst.append(name)
    
    return data_lst



def load_data_player(name): 
    path = os.environ.get("LOCALAPPDATA") + "\\Kerosine"

    if not os.path.exists(path):
        return False
    
    path_file = path + "\\" + name + ".json"

    if not os.path.exists(path_file):
        return False
    
    with open(path_file, "r") as f:
        player_info = json.load(f)
    
    return player_info


def del_data_player(name) -> bool:
    path = os.environ.get("LOCALAPPDATA") + "\\Kerosine"

    if not os.path.exists(path):
        return False
    
    path_file = path + "\\" + name + ".json"

    if not os.path.exists(path_file):
        return False

    os.remove(path_file)
    return True


def save(data_user: dict) -> None:
    path = os.environ.get("LOCALAPPDATA") + "\\Kerosine"
    
    if not os.path.exists(path):
        os.mkdir(path)

    name_file = data_user.get("name") + ".json"
    
    path = path + "\\" + name_file

    with open(path, "w") as f:
        json.dump(data_user, f)