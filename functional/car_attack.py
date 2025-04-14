import random
from gui import view
import time


def car_fight(player):
    # Создание соперника
    car = generate_car(player["difficulty"])
    view.info_car(car)

    # Процесс боя с машиной
    fight = True
    while fight:

        # Начать или пропустить бой
        selection_attack = view.user_input()
        if selection_attack.lower().replace(" ", "") == "да":

            # Подготовка к бою
            item_name = view.select_items(player)
            if item_name == "menu":
                return "menu"

            elif item_name == "exit":
                return "exit"
        
            # Бой
            result = attack(player, item_name, car)

            # Обработка результатов боя
            if result[0] == "bomb":
                view.output_stage("car_boom")

            elif result[0] == "destroy":
                view.output_stage("destroy")

            elif result[0] == "car_save":
                view.output_stage("car_save")

                repeat = select_player(player)
                if repeat:
                    continue

            return result

        elif selection_attack.lower() == "нет":
            return "next"

        else:
            view.output_info("not_command")



def attack(plr, items, car):
    # Удаление предметов из инвентаря
    dps = 0
    num_item = 0
    for i in plr["inventory"]:
        items_list = plr["inventory"][i]
        for j in range(len(items_list)):
            if items_list[j]["name"].replace(" ", "") == items[num_item].replace(" ", ""):
                dps += items_list[j]["damage"]
                items_list.pop(j)
                break
        num_item += 1
    
    # Выбор остаться у машины или отойти от неё
    move_away = None
    view.output_action("select_move_away")

    while move_away == None:
        user_select = view.user_input().lower().replace(" ", "")
        if user_select == "нет":
            move_away = True
        
        elif user_select == "да":
            move_away = False

        else:
            view.output_info("not_command")

    # Атака авто
    while car["health"] > 0:
        flag_boom = random.randint(1, 100) > 97
        flag_extinguishing = random.randint(1, 100) > 980
        flag_krit = random.randint(1,100) > 70

        if flag_boom:
            car["health"] = 0

            if move_away:
                plr["health"] -= 10
            
            else:
                plr["health"] -= 30

            view.output_stage("bomb")

            return "bomb", move_away

        if flag_extinguishing:
            view.output_stage("extinguishing")
            return "car_save", move_away
        
        damage = damage_car(car, flag_krit, dps, plr["difficulty"])

        if not move_away:
            plr["health"] -= 2
            view.output_action("damage_plr_for_fire")
            time.sleep(2)

        view.output_attack_info(car, damage)
        
    return "destroy", move_away


def select_player(plr):
    if plr["inventory"]["bootle"]:
        while True:
            view.output_stage("repeat_fire")
            select = view.user_input()

            if select.lower().replace(" ", "") == "дожечь":
                return True
            
            elif select.lower().replace(" ", "") == "дальше":
                return False
            
            else: 
                view.output_info("not_command")


def damage_car(car, krit, dps, diff):
    match diff:
        case "easy":
            if krit:
                car["health"] = car["health"] - dps * 3
                return dps * 3
            else:
                car["health"] = car["health"] - dps
                return dps

        case "medium":
            if krit:
                car["health"] = car["health"] - dps + 5 * 3
                return dps + 5 * 3
            else:
                car["health"] = car["health"] - dps + 5
                return dps + 5

        case "hard":
            if krit:
                car["health"] = car["health"] - dps + 10 * 3
                return dps + 10 * 3
            else:
                car["health"] = car["health"] - dps + 10
                return dps + 10

        case "extreme":
            if krit:
                car["health"] = car["health"] - dps + 25 * 3
                return dps + 25 * 3
            else:
                car["health"] = car["health"] - dps + 25
                return dps + 25

        case "master":
            if krit:
                car["health"] = car["health"] - dps + 20 * 3
                return dps + 20 * 3
            else:
                car["health"] = car["health"] - dps + 20
                return dps + 20

        case "kara":
            if krit:
                car["health"] = car["health"] - dps + 30 * 3
                return dps + 30 * 3
            else:
                car["health"] = car["health"] - dps + 30
                return dps + 30


def generate_car(diff):
    car_names = ["Range Rover", "Ford Focus", "Mustang", "Cobalt", "BMW M5", "BMW X3", "Mercedes", "KIA RIO", "Suzuki Aventa", "Lamborgini",
       "Mercedes Benz", "Bugatti", "Ferrari", "Jaguar", "Tesla", "Nussan Qasqai", "Toyota corolla", "Camry 3.5", "BMW E34", "Priora",
       "Lada Granta", "Huyndai Elantra", "Huyndai Solaris", "Matiz", "Nexia", "Porshe", "Chevrolet Cruze", "Camaro", "Corvette", "Polo", 
       "Passat", "ВАЗ 2114", "ВАЗ 2106", "Калина", "Bentley", "Panamera", "Audi R8", "Audi Q8", "Audi 80", "Nissan RX8", "Honda Accord"]


    data_diff = {
        "easy" : [40, 70, 3, 5],
        "medium" : [70, 100, 5, 7],
        "hard" : [100, 250, 7, 10],
        "master" : [250, 300, 10, 15],
        "extreme" : [300, 500, 15, 25],
        "kara" : [500, 1500, 25, 50] 
    }

    car = {
        "name_car" : random.choice(car_names),
        "health" : random.randint(data_diff[diff][0], data_diff[diff][1]),
        "deff" : random.randint(data_diff[diff][2], data_diff[diff][3])
        } 
    
    return car
