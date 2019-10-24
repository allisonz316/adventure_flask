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
    world["character_current_hp"] = INITIAL_WORLD["current_hp"]
    world["character_total_hp"] = INITIAL_WORLD["total_hp"]
    world["character_def"] = INITIAL_WORLD["def"]
    world["character_exp"] = INITIAL_WORLD["exp"]
    world["character_lvl"] = INITIAL_WORLD["lvl"]
    world["inventory_one"] = INITIAL_WORLD["inventory_slot_one"]
    world["inventory_two"] = INITIAL_WORLD["inventory_slot_two"]
    world["inventory_three"] = INITIAL_WORLD["inventory_slot_three"]
    world["inventory_four"] = INITIAL_WORLD["inventory_slot_four"]
    world["weapon"] = INITIAL_WORLD["weapons"]
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
        return render_template("enter_forest.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], item3=world["inventory_three"],
                               item4=world["inventory_four"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"])
    elif where == "give_up":
        return render_template("give_up.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], item3=world["inventory_three"],
                               item4=world["inventory_four"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"])
    elif where == "clearing":
        return render_template("clearing.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], item3=world["inventory_three"],
                               item4=world["inventory_four"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"])
    elif where == "lake":
        return render_template("lake.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], item3=world["inventory_three"],
                               item4=world["inventory_four"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"])


@simple_route("/your_turn/<current_monster>/")
def your_turn(world: dict, current_monster: str):
    if world["character_current_hp"] <= 0:
        if world["character_current_hp"] < 0:
            world["character_current_hp"] = 0
        return render_template("game_over.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], item3=world["inventory_three"],
                               item4=world["inventory_four"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"])
    else:
        return render_template("your_turn.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], item3=world["inventory_three"],
                               item4=world["inventory_four"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"],
                               current_monster=current_monster)


@simple_route("/first_turn/<current_monster>/")
def first_turn(world: dict, current_monster: str):
    return render_template("first_turn.html", item1=world["inventory_one"],
                           item2=world["inventory_two"], item3=world["inventory_three"],
                           item4=world["inventory_four"], weapon=world["weapon"],
                           current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                           experience=world["character_exp"], level=world["character_lvl"], current_monster=current_monster)


@simple_route("/battle/<current_monster>/")
def battle(world: dict, current_monster: str):
    if world["monster_hp"] <= 0:
        if world["location"] == "left":
            where = "clearing"
        elif world["location"] == "right":
            where = "lake"
        world["character_exp"] = world["character_exp"] + world["monster_exp_drop"]
        world["character_current_hp"] = world["character_total_hp"]
        if world["character_exp"] >= 50:
            world["character_lvl"] = world["character_lvl"] + 1
            world["character_exp"] = world["character_exp"] - 50
            world["character_total_hp"] = world["character_total_hp"] + 5
            world["character_current_hp"] = world["character_total_hp"]
            world["character_def"] = world["character_def"] + 1
            return render_template("battle_victory_level_up.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"],
                                   item3=world["inventory_three"],
                                   item4=world["inventory_four"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster, exp=world["monster_exp_drop"],
                                   where=where)
        else:
            return render_template("battle_victory.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"], item3=world["inventory_three"],
                                   item4=world["inventory_four"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster, exp=world["monster_exp_drop"],
                                   where=where)
    else:
        atk = world["monster_atk"] - 2
        atk2 = world["monster_atk"] + 1
        damage = random.randrange(atk, atk2)
        world["character_current_hp"] = world["character_current_hp"] - damage
        if world["character_current_hp"] < 0:
            world["character_current_hp"] = 0
        return render_template("monster_turn.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], item3=world["inventory_three"],
                               item4=world["inventory_four"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"],
                               current_monster=current_monster, damage=damage, hp=world["character_current_hp"])


@simple_route("/attack/<current_monster>/")
def attack(world: dict, current_monster: str):
    if world["weapon"] == "Sword":
        damage = random.randrange(4, 7)
        world["monster_hp"] = world["monster_hp"] - damage
        return render_template("attack.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], item3=world["inventory_three"],
                               item4=world["inventory_four"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"],
                               current_monster=current_monster, damage=damage, hp=world["monster_hp"])


@simple_route("/heal/<current_monster>/")
def heal(world: dict, current_monster: str):
    if world["character_current_hp"] < world["character_total_hp"]:
        if world["inventory_one"] == "Potion":
            world["character_current_hp"] = world["character_current_hp"] + 10
            if world["character_current_hp"] > world["character_total_hp"]:
                world["character_current_hp"] = world["character_total_hp"]
            world["inventory_one"] = "Empty"
            return render_template("heal.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"],
                                   item3=world["inventory_three"],
                                   item4=world["inventory_four"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster)
        elif world["inventory_two"] == "Potion":
            world["character_current_hp"] = world["character_current_hp"] + 10
            if world["character_current_hp"] > world["character_total_hp"]:
                world["character_current_hp"] = world["character_total_hp"]
            world["inventory_two"] = "Empty"
            return render_template("heal.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"],
                                   item3=world["inventory_three"],
                                   item4=world["inventory_four"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster)
        elif world["inventory_three"] == "Potion":
            world["character_current_hp"] = world["character_current_hp"] + 10
            if world["character_current_hp"] > world["character_total_hp"]:
                world["character_current_hp"] = world["character_total_hp"]
            world["inventory_three"] = "Empty"
            return render_template("heal.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"],
                                   item3=world["inventory_three"],
                                   item4=world["inventory_four"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster)
        elif world["inventory_four"] == "Potion":
            world["character_current_hp"] = world["character_current_hp"] + 10
            if world["character_current_hp"] > world["character_total_hp"]:
                world["character_current_hp"] = world["character_total_hp"]
            world["inventory_four"] = "Empty"
            return render_template("heal.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"],
                                   item3=world["inventory_three"],
                                   item4=world["inventory_four"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster)
        else:
            return render_template("heal_fail1.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"],
                                   item3=world["inventory_three"],
                                   item4=world["inventory_four"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster)
    else:
        return render_template("heal_fail2.html", item1=world["inventory_one"],
                               item2=world["inventory_two"],
                               item3=world["inventory_three"],
                               item4=world["inventory_four"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"],
                               current_monster=current_monster)


@simple_route("/flee/<current_monster>/")
def flee(world: dict, current_monster: str):
    flee_chance = random.randrange(1, 11)
    if flee_chance >= 7:
        return render_template("flee_success.html", item1=world["inventory_one"],
                               item2=world["inventory_two"],
                               item3=world["inventory_three"],
                               item4=world["inventory_four"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"],
                               current_monster=current_monster)
    else:
        return render_template("flee_fail.html", item1=world["inventory_one"],
                               item2=world["inventory_two"],
                               item3=world["inventory_three"],
                               item4=world["inventory_four"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"],
                               current_monster=current_monster)


@simple_route("/generate/monster/<where>/")
def generate_monster(world: dict, where: str) -> str:
    monster_number = random.randrange(1, 10)
    current_monster = ""
    monster_hp = 0
    monster_atk = 0
    monster_exp_drop = 0
    image = ""
    height = "250"
    if monster_number == 1:
        current_monster = "Gel-O"
        monster_hp = 7
        monster_atk = 4
        monster_exp_drop = 3
        image = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/95c81da5-abd3-499e-bb71-a32be4435115/d38yzcn-be11f801-06e2-4d96-bd13-483c1493b971.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzk1YzgxZGE1LWFiZDMtNDk5ZS1iYjcxLWEzMmJlNDQzNTExNVwvZDM4eXpjbi1iZTExZjgwMS0wNmUyLTRkOTYtYmQxMy00ODNjMTQ5M2I5NzEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.6yDXL-r4fgQwWe3JJk2z5jxZAk0NVIDEPy2VD-hUZhw"
    elif monster_number == 2:
        current_monster = "Beehat"
        monster_hp = 12
        monster_atk = 6
        monster_exp_drop = 5
        image = "https://images4-g.ravelrycache.com/uploads/LuckyFoxKnits/549000002/Second_cover_small2.jpg"
    elif monster_number == 3:
        current_monster = "Socktorok"
        monster_hp = 15
        monster_atk = 5
        monster_exp_drop = 6
        image = "https://images4-g.ravelrycache.com/uploads/kjbrasda/244331547/DSCF7897_small2.JPG"
    elif monster_number == 4:
        current_monster = "Beever"
        monster_hp = 8
        monster_atk = 3
        monster_exp_drop = 4
        height = "300"
        image = "https://img.huffingtonpost.com/asset/5cd6f6ee2100005800c86c95.jpeg?ops=scalefit_630_noupscale"
    elif monster_number == 5:
        current_monster = "Dinofloss"
        monster_hp = 14
        monster_atk = 7
        monster_exp_drop = 8
        image = "https://images-na.ssl-images-amazon.com/images/I/51T0TWGJYQL._SY355_.jpg"
    elif monster_number == 6:
        current_monster = "Wolfy"
        monster_hp = 18
        monster_atk = 8
        monster_exp_drop = 10
        image = "https://66.media.tumblr.com/f927883b6fe0f9547b063f53b02e1428/tumblr_mgs171WwBy1rwcfrqo5_250.jpg"
    elif monster_number == 7:
        current_monster = "Dingdongo"
        monster_hp = 17
        monster_atk = 7
        monster_exp_drop = 12
        image = "https://images-na.ssl-images-amazon.com/images/I/51QnDuSzMqL.jpg"
    elif monster_number == 8:
        current_monster = "Kee"
        monster_hp = 6
        monster_atk = 3
        monster_exp_drop = 2
        image = "https://vignette.wikia.nocookie.net/clubpenguin/images/e/ea/7126_icon.png/revision/latest?cb=20121004074608"
    elif monster_number == 9:
        current_monster = "Wizzo"
        monster_hp = 10
        monster_atk = 7
        monster_exp_drop = 8
        height = "300"
        image = "https://www.how-to-draw-funny-cartoons.com/images/wizard-clipart-004.png"
    world["monster"] = current_monster
    world["monster_hp"] = monster_hp
    world["monster_atk"] = monster_atk
    world["monster_exp_drop"] = monster_exp_drop
    world["monster_image"] = image
    world["monster_image_height"] = height
    world["location"] = where
    return render_template("monster.html", item1=world["inventory_one"], item2=world["inventory_two"], item3=world["inventory_three"],
                           item4=world["inventory_four"], weapon=world["weapon"], current_hp=world["character_current_hp"],
                           total_hp=world["character_total_hp"], experience=world["character_exp"],
                           level=world["character_lvl"], name=world["monster"], where=where, image=world["monster_image"],
                           height=world["monster_image_height"])
