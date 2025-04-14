from gui.dictions import dictions_info
from gui.dictions import dictions_action
from gui.dictions import dictions_stage
from gui import settings


def output_info(key=None):
    print(dictions_info.dict[key])


def output_stage(key=None):
    print(dictions_stage.dict[key])


def output_action(key=None):
    print(dictions_action.dict[key])


def user_input():
    data = input("->> ")
    print()
    return data

def output_profile(data):
    for name in data:
        print(f"\t{name}")


def output_new_game_info(name_player):
    import time


    print(f"Ты что задумал, {name_player}? Ты хочешь сжечь машины соседей?? \nИ что это такое в сумке? Бутылка керосина и зажигалка которую подарила тебе мама?\n" +
          "Да, точно... Она самая\n")
    time.sleep(2)
    print(f"Ну что-ж, тогда твоя задача, {name_player}, выйти на улицу ночью пока соседи не видят, поджечь их машины и скрыться, понял?\n")
    time.sleep(2)
    print("Время на часах 00:00. Ты понимаешь, что это значит? Время для того, чтобы исполнить задуманное...\n")
    time.sleep(2)
    print("Ты вернулся домой? Погоди, как ты мог забыть бутылку керосина? И хватит думать, решайся уже...\n")
    time.sleep(2)
    print("Раз решился, давай делать задуманное! Воплощай идеи в жизнь!\n")
    time.sleep(2)
    print(f"Вот твоя бутылка, {name_player}, положи её в 'Инвентарь', туда же, где лежит зажигалка. Удачи!\n")
    time.sleep(2)
    print(f"Ты точно помнишь, сколько соседей над тобой издевались, а поэтому, {name_player}, ты понимаешь, скольно нужно сжечь машин...\n")


def info_car(car):
    print(f"Перед тобой {car['name_car']}. У него {car["health"]} здоровья, его показатель защиты = {car['deff']}")
    output_stage("prepare")

def select_items(player):
    inventory = player["inventory"]

    # Вывод текущих бутылок керосина пользователя
    print("Сейчас у тебя есть из бутылок:")
    list_bottle = []
    for i in inventory["bottle"]:
        print(f"\n{i['name']}")
        list_bottle.append(i['name'].lower().replace(" ", ""))
    
    while True:
        print("\nВыбери что хочешь использовать:")

        bottle_name = user_input()

        if bottle_name.lower().replace(" ", "") in list_bottle:
            break

        elif bottle_name.lower().replace(" ", "") == "menu":
            return "menu"

        elif bottle_name.lower().replace(" ", "") == "exit":
            return "exit"
        
        else: 
            output_info("not_command")

    # Вывод текущих зажигалок пользователя
    print("Из зажигалок у тебя есть:")
    list_lighter = []
    for i in inventory["lighter"]:
        print(f"\n{i['name']}")
        list_lighter.append(i['name'].lower().replace(" ", ""))

    while True:
        print("\nВыбери что хочешь использовать:")
        
        lighter_name = user_input()

        if lighter_name.lower().replace(" ", "") in list_lighter:
            break

        elif bottle_name.lower().replace(" ", "") == "menu":
            return "menu"

        elif bottle_name.lower().replace(" ", "") == "exit":
            return "exit"
        
        else: 
            output_info("not_command")

    return bottle_name, lighter_name


def output_attack_info(car, dmg):
    print(f"Машина получила {dmg} урона! Осталось {car['health'] if car["health"]>= 0 else 0} здоровья!\n")

def output_loop(result):
    print(f"Зацени! Ты получил по {result[0]} бутылки и зажигалки")
    if result[1]:
        print("А еще мы нашли аптечку! Подлатаем тебя и идем к следующей карме =)")