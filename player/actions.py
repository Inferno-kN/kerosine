from player import player_info
from items import items_info
import random


def set_difficulty(player):
    if player["destroyed_cars"] >= 10 and player["destroyed_cars"] <= 30:
        player["difficulty"] = "medium"

    elif player["destroyed_cars"] >= 30 and player["destroyed_cars"] <= 50:
        player["difficulty"] = "hard"

    elif player["destroyed_cars"] >= 50 and player["destroyed_cars"] <= 70:
        player["difficulty"] = "master"

    elif player["destroyed_cars"] >= 70 and player["destroyed_cars"] <= 90:
        player["difficulty"] = "extreme"

    elif player["destroyed_cars"] > 90:
        player["difficulty"] = "kara"


def loot_drop(player, result_car, result_neighbor):
    loot = 1
    
    if result_car[0] == "destroy" and not result_car[1]:
            loot += 1

    if result_neighbor:
        loot += 1

    for bootle in range(loot):
        select = random.choice(list(items_info.items_bootle.keys()))
        player["inventory"]["bottle"].append(items_info.items_bootle[select])

    for lighter in range(loot):
        select = random.choice(list(items_info.items_light.keys()))
        player["inventory"]["lighter"].append(items_info.items_light[select])
    
    if loot > 2:
        result = random.randint(0, 10) > 8
        item = random.choice(list(items_info.med_kit.keys()))
        player["health"] += items_info.med_kit[item]["damage"]

        med_kit = True

    else:
        med_kit = False

    return loot, med_kit

