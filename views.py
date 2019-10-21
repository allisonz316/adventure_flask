from route_helper import simple_route
from route_helper import INITIAL_WORLD
from flask import render_template
import random


@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    world["current_hp"] = INITIAL_WORLD["current_hp"]
    world["total_hp"] = INITIAL_WORLD["total_hp"]
    world["def"] = INITIAL_WORLD["def"]
    world["exp"] = INITIAL_WORLD["exp"]
    world["lvl"] = INITIAL_WORLD["lvl"]
    world["inventory_slot_one"] = INITIAL_WORLD["inventory_slot_one"]
    world["inventory_slot_two"] = INITIAL_WORLD["inventory_slot_two"]
    world["inventory_slot_three"] = INITIAL_WORLD["inventory_slot_three"]
    world["inventory_slot_four"] = INITIAL_WORLD["inventory_slot_four"]
    world["weapons"] = INITIAL_WORLD["weapons"]
    return render_template("index.html", item1=world["inventory_one"],
                           item2=world["inventory_two"], item3=world["inventory_three"],
                           item4=world["inventory_four"], weapon=world["weapon"],
                           current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                           experience=world["character_exp"], level=world["character_lvl"])


@simple_route('/goto/<where>/')
def open_door(world: dict, where: str) -> str:
    """
    Update the player location

    :param world: The current world
    :param where: The new location to move to
    :return: The HTML to show the player
    """
    world['location'] = where
    if where == "forest":
        return render_template("enter_forest.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"])
    elif where == "give_up":
        return render_template("give_up.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"])


@simple_route("/your_turn/<current_monster>/")
def your_turn(world: dict, current_monster: str):
    return render_template("your_turn.html", item1=world["inventory_slot_one"],
                           item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                           item4=world["inventory_slot_four"], weapon=world["weapons"],
                           current_hp=world["current_hp"], total_hp=world["total_hp"],
                           experience=world["exp"], level=world["lvl"], current_monster=current_monster)


@simple_route("/first_turn/<current_monster>/")
def first_turn(world: dict, current_monster: str):
    return render_template("first_turn.html", item1=world["inventory_slot_one"],
                           item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                           item4=world["inventory_slot_four"], weapon=world["weapons"],
                           current_hp=world["current_hp"], total_hp=world["total_hp"],
                           experience=world["exp"], level=world["lvl"], current_monster=current_monster)


@simple_route("/battle/<current_monster>/")
def battle(world: dict, current_monster: str):
    if world["monster_hp"] <= 0:
        world["exp"] = world["exp"] + world["monster_exp_drop"]
        world["current_hp"] = world["total_hp"]
        if world["exp"] >= 50:
            world["lvl"] = world["lvl"] + 1
            world["exp"] = world["exp"] - 50
            world["total_hp"] = world["total_hp"] + 5
            world["current_hp"] = world["total_hp"]
            world["def"] = world["def"] + 1
            return render_template("battle_victory_level_up.html", item1=world["inventory_slot_one"],
                                   item2=world["inventory_slot_two"],
                                   item3=world["inventory_slot_three"],
                                   item4=world["inventory_slot_four"], weapon=world["weapons"],
                                   current_hp=world["current_hp"], total_hp=world["total_hp"],
                                   experience=world["exp"], level=world["lvl"],
                                   current_monster=current_monster, exp=world["monster_exp_drop"])
        else:
            return render_template("battle_victory.html", item1=world["inventory_slot_one"],
                                   item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                                   item4=world["inventory_slot_four"], weapon=world["weapons"],
                                   current_hp=world["current_hp"], total_hp=world["total_hp"],
                                   experience=world["exp"], level=world["lvl"],
                                   current_monster=current_monster, exp=world["monster_exp_drop"])
    else:
        atk = world["monster_atk"] - 2
        atk2 = world["monster_atk"] + 1
        damage = random.randrange(atk, atk2)
        world["current_hp"] = world["current_hp"] - damage
        return render_template("monster_turn.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"],
                               current_monster=current_monster, damage=damage, hp=world["current_hp"])


@simple_route("/attack/<current_monster>/")
def attack(world: dict, current_monster: str):
    if world["weapons"] == "Sword":
        damage = random.randrange(4, 7)
        world["monster_hp"] = world["monster_hp"] - damage
        return render_template("attack.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"],
                               current_monster=current_monster, damage=damage, hp=world["monster_hp"])


@simple_route("/heal/<current_monster>/")
def heal(world: dict, current_monster: str):
    if world["current_hp"] < world["total_hp"]:
        if world["inventory_slot_one"] == "Potion":
            world["current_hp"] = world["current_hp"] + 10
            if world["current_hp"] > world["total_hp"]:
                world["current_hp"] = world["total_hp"]
            world["inventory_slot_one"] = "Empty"
            return render_template("heal.html", item1=world["inventory_slot_one"],
                                   item2=world["inventory_slot_two"],
                                   item3=world["inventory_slot_three"],
                                   item4=world["inventory_slot_four"], weapon=world["weapons"],
                                   current_hp=world["current_hp"], total_hp=world["total_hp"],
                                   experience=world["exp"], level=world["lvl"],
                                   current_monster=current_monster)
        elif world["inventory_slot_two"] == "Potion":
            world["current_hp"] = world["current_hp"] + 10
            if world["current_hp"] > world["total_hp"]:
                world["current_hp"] = world["total_hp"]
            world["inventory_slot_two"] = "Empty"
            return render_template("heal.html", item1=world["inventory_slot_one"],
                                   item2=world["inventory_slot_two"],
                                   item3=world["inventory_slot_three"],
                                   item4=world["inventory_slot_four"], weapon=world["weapons"],
                                   current_hp=world["current_hp"], total_hp=world["total_hp"],
                                   experience=world["exp"], level=world["lvl"],
                                   current_monster=current_monster)
        elif world["inventory_slot_three"] == "Potion":
            world["current_hp"] = world["current_hp"] + 10
            if world["current_hp"] > world["total_hp"]:
                world["current_hp"] = world["total_hp"]
            world["inventory_slot_three"] = "Empty"
            return render_template("heal.html", item1=world["inventory_slot_one"],
                                   item2=world["inventory_slot_two"],
                                   item3=world["inventory_slot_three"],
                                   item4=world["inventory_slot_four"], weapon=world["weapons"],
                                   current_hp=world["current_hp"], total_hp=world["total_hp"],
                                   experience=world["exp"], level=world["lvl"],
                                   current_monster=current_monster)
        elif world["inventory_slot_four"] == "Potion":
            world["current_hp"] = world["current_hp"] + 10
            if world["current_hp"] > world["total_hp"]:
                world["current_hp"] = world["total_hp"]
            world["inventory_slot_four"] = "Empty"
            return render_template("heal.html", item1=world["inventory_slot_one"],
                                   item2=world["inventory_slot_two"],
                                   item3=world["inventory_slot_three"],
                                   item4=world["inventory_slot_four"], weapon=world["weapons"],
                                   current_hp=world["current_hp"], total_hp=world["total_hp"],
                                   experience=world["exp"], level=world["lvl"],
                                   current_monster=current_monster)
        else:
            return render_template("heal_fail1.html", item1=world["inventory_slot_one"],
                                   item2=world["inventory_slot_two"],
                                   item3=world["inventory_slot_three"],
                                   item4=world["inventory_slot_four"], weapon=world["weapons"],
                                   current_hp=world["current_hp"], total_hp=world["total_hp"],
                                   experience=world["exp"], level=world["lvl"],
                                   current_monster=current_monster)
    else:
        return render_template("heal_fail2.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"],
                               item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"],
                               current_monster=current_monster)


@simple_route("/flee/<current_monster>/")
def flee(world: dict, current_monster: str):
    flee_chance = random.randrange(1, 11)
    if flee_chance >= 7:
        return render_template("flee_success.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"],
                               item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"],
                               current_monster=current_monster)
    else:
        return render_template("flee_fail.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"],
                               item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"],
                               current_monster=current_monster)


@simple_route("/generate/monster/<where>/")
def generate_monster(world: dict, where: str) -> str:
    monster_number = random.randrange(1, 10)
    current_monster = ""
    monster_hp = 0
    monster_atk = 0
    monster_exp_drop = 0
    if monster_number == 1:
        current_monster = "Gel-O"
        monster_hp = 7
        monster_atk = 4
        monster_exp_drop = 3
    elif monster_number == 2:
        current_monster = "Beehat"
        monster_hp = 12
        monster_atk = 6
        monster_exp_drop = 5
    elif monster_number == 3:
        current_monster = "Socktorok"
        monster_hp = 15
        monster_atk = 5
        monster_exp_drop = 6
    elif monster_number == 4:
        current_monster = "Beever"
        monster_hp = 8
        monster_atk = 3
        monster_exp_drop = 4
    elif monster_number == 5:
        current_monster = "Dinofloss"
        monster_hp = 14
        monster_atk = 7
        monster_exp_drop = 8
    elif monster_number == 6:
        current_monster = "Wolfy"
        monster_hp = 18
        monster_atk = 8
        monster_exp_drop = 10
    elif monster_number == 7:
        current_monster = "Dingdongo"
        monster_hp = 17
        monster_atk = 7
        monster_exp_drop = 12
    elif monster_number == 8:
        current_monster = "Key"
        monster_hp = 6
        monster_atk = 3
        monster_exp_drop = 2
    elif monster_number == 9:
        current_monster = "Wizzo"
        monster_hp = 10
        monster_atk = 7
        monster_exp_drop = 8
    world["monster"] = current_monster
    world["monster_hp"] = monster_hp
    world["monster_atk"] = monster_atk
    world["monster_exp_drop"] = monster_exp_drop
    world["location"] = where
    if monster_number == 1:
        return render_template("monster1.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"], name=current_monster,
                               where=where)
    elif monster_number == 2:
        return render_template("monster2.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"], name=current_monster,
                               where=where)
    elif monster_number == 3:
        return render_template("monster3.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"], name=current_monster,
                               where=where)
    elif monster_number == 4:
        return render_template("monster4.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"], name=current_monster,
                               where=where)
    elif monster_number == 5:
        return render_template("monster5.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"], name=current_monster,
                               where=where)
    elif monster_number == 6:
        return render_template("monster6.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"], name=current_monster,
                               where=where)
    elif monster_number == 7:
        return render_template("monster7.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"], name=current_monster,
                               where=where)
    elif monster_number == 8:
        return render_template("monster8.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"], name=current_monster,
                               where=where)
    elif monster_number == 9:
        return render_template("monster9.html", item1=world["inventory_slot_one"],
                               item2=world["inventory_slot_two"], item3=world["inventory_slot_three"],
                               item4=world["inventory_slot_four"], weapon=world["weapons"],
                               current_hp=world["current_hp"], total_hp=world["total_hp"],
                               experience=world["exp"], level=world["lvl"], name=current_monster,
                               where=where)
