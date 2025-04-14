from player import actions as plr_func
from functional import car_attack, neighbor_attack
from gui import view
import random
from conservation.saveLoad import save


def run_game(player_info: dict):
    game = True
    while game:
        # Вывод в случае если новая игра
        if player_info.get("new", False):
            view.output_new_game_info(player_info["name"])
            player_info.pop("new")

        # Установить текущую сложность игры
        plr_func.set_difficulty(player_info)

        # Процесс боя с машиной
        result_fight_car = car_attack.car_fight(player_info)

        if result_fight_car == "menu":
            return result_fight_car
        
        elif result_fight_car == "exit":
            return result_fight_car

        live_resilt = player_info["health"] >= 0
        if not live_resilt:
            view.output_info("dead")
            return "theend"

        # Появление соседа (с шансом 30%)
        if player_info["difficulty"] == "easy":
            flag_neighbor = random.randint(1, 100) > 90
        if player_info["difficulty"] == "medium":
            flag_neighbor = random.randint(1, 100) > 85
        if player_info["difficulty"] == "hard":
            flag_neighbor = random.randint(1, 100) > 80
        if player_info["difficulty"] == "master":
            flag_neighbor = random.randint(1, 100) > 75
        if player_info["difficulty"] == "extreme":
            flag_neighbor = random.randint(1, 100) > 50
        else:
            flag_neighbor = True

        # ---
        if flag_neighbor: 
            result_fight_neighbor = neighbor_attack.neighbor_fight(player_info)
            if result_fight_neighbor == "menu":
                return result_fight_neighbor
            
            elif result_fight_neighbor == "exit":
                return result_fight_neighbor
            
        else:
            result_fight_neighbor = False

        live_resilt = player_info["health"] >= 0
        if not live_resilt:
            view.output_info("dead")
            return "theend"

        # Сбор наград с боя
        result_loop = plr_func.loot_drop(player_info, result_fight_car, result_fight_neighbor)
        view.output_loop(result_loop)


        # Сохранение текущей игры
        save(player_info)
        

        
        