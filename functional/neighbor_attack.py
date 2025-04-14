from gui import view
import random

def neighbor_fight(plr):
    # Сообщение о появлении соседа
    view.output_stage("neighbor_preview")
    while True:
        select = view.user_input()
        if select.lower().replace(" ", "") == "бежать":
            return False

        elif select.lower().replace(" ", "") == "мстить":
            break
        
        elif select.lower().replace(" ", "") == "menu":
            return "menu"
        
        elif select.lower().replace(" ", "") == "exit":
            return "exit"
        
        else: 
            view.output_info("menu")

    # Развязка
    win = result_fight(plr.get("difficulty"))

    # Сверка результатов
    if not win:
        view.output_info("lose_neighbor")
        plr["health"] -= 15
        result = False
    
    else:
        view.output_info("win_neighbor")
        result = True

    # Возврат результата
    return result


def result_fight(diff):
    data_diff = {
        "easy" : 10,
        "medium" : 15,
        "hard" : 20,
        "master" : 25,
        "extreme" : 30,
        "kara" : 50 
    }

    status = random.randint(0, 100) < data_diff[diff]

    return  status