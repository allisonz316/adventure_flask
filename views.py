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
    world["weapon"] = INITIAL_WORLD["weapons"]
    return render_template("index.html", item1=world["inventory_one"],
                           item2=world["inventory_two"], weapon=world["weapon"],
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
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"])
    elif where == "give_up":
        return render_template("give_up.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"])
    elif where == "clearing":
        return render_template("clearing.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"])
    elif where == "lake":
        return render_template("lake.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"])
    elif where == "deep forest":
        return render_template("deep_forest.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "lake island":
        return render_template("lake_island.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "pre Phantom Gonandarf Boss Fight":
        return render_template("weapon_intro.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "pre Merph Boss Fight":
        return render_template("weapon_intro.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "Phantom Gonandarf Boss Fight":
        return render_template("phantom_gonandarf.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "Merph Boss Fight":
        return render_template("merph.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "post Phantom Gonandarf Boss Fight":
        return render_template("weapon_intro.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "post Merph Boss Fight":
        return render_template("weapon_intro.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "forest temple":
        return render_template("forest_temple.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "lake temple":
        return render_template("lake_temple.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "pre Kaleidoscope Boss Fight":
        return render_template("weapon_intro.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "pre Gurg Boss Fight":
        return render_template("weapon_intro.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "Kaleidoscope Boss Fight":
        return render_template("kaleidoscope.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "Gurg Boss Fight":
        return render_template("gurg.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "forest tunnel":
        return render_template("forest_tunnel.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "lake tunnel":
        return render_template("lake_tunnel.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "pre Gonandarf Boss Fight":
        return render_template("weapon_intro.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "Gonandarf Boss Fight":
        return render_template("gonandarf.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])
    elif where == "endgame":
        return render_template("endgame.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], where=world["location"])


@simple_route("/weapon/<where>/")
def weapon_get(world: dict, where: str):
    """
        Gives the player a new weapon

        :param world: The current world
        :param where: The current location
        :return: The HTML to show the player
        """
    new_weapon = ""
    if world["location"] == "pre Gonandarf Boss Fight":
        new_weapon = "Masterful Sword"
        world["location"] = "Gonandarf Boss Fight"
    elif world["location"] == "pre Kaleidoscope Boss Fight":
        new_weapon = "Even Superer Sword"
        world["location"] = "Kaleidoscope Boss Fight"
    elif world["location"] == "pre Gurg Boss Fight":
        new_weapon = "Even Superer Sword"
        world["location"] = "Gurg Boss Fight"
    elif world["location"] == "post Phantom Gonandarf Boss Fight":
        new_weapon = "Superer Sword"
        world["location"] = "forest temple"
    elif world["location"] == "post Merph Boss Fight":
        new_weapon = "Superer Sword"
        world["location"] = "lake temple"
    elif world["location"] == "pre Phantom Gonandarf Boss Fight":
        new_weapon = "Super Sword"
        world["location"] = "Phantom Gonandarf Boss Fight"
    elif world["location"] == "pre Merph Boss Fight":
        new_weapon = "Super Sword"
        world["location"] = "Merph Boss Fight"
    world["weapon"] = new_weapon
    return render_template("weapon_get.html", item1=world["inventory_one"],
                           item2=world["inventory_two"], weapon=world["weapon"],
                           current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                           experience=world["character_exp"], level=world["character_lvl"], where=world["location"],
                           new_weapon=new_weapon)


@simple_route("/chest/<item>/")
def open_chest(world: dict, item: str):
    """
        Adds a new item to player's inventory

        :param world: The current world
        :param item: Which item is being obtained
        :return: The HTML to show the player
        """
    if world["location"] == "clearing":
        world["location"] = "deep forest"
    elif world["location"] == "lake":
        world["location"] = "lake island"
    elif world["location"] == "forest tunnel" or world["location"] == "lake tunnel":
        world["location"] = "pre Gonandarf Boss Fight"
    if world["inventory_one"] == "Empty":
        world["inventory_one"] = item
    elif world["inventory_two"] == "Empty":
        world["inventory_two"] = item
    else:
        return render_template("inventory_full.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], item=item,
                               where=world["location"])
    return render_template("chest.html", item1=world["inventory_one"],
                           item2=world["inventory_two"], weapon=world["weapon"],
                           current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                           experience=world["character_exp"], level=world["character_lvl"], item=item,
                           where=world["location"])


@simple_route("/swap/<slot>/<item>/")
def item_swap(world: dict, slot: str, item: str):
    """
        Replaces old item in inventory with new item

        :param world: The current world
        :param slot: Which slot the new item will fill
        :param item: Which item is being obtained
        :return: The HTML to show the player
        """
    if slot == "one":
        world["inventory_one"] = item
        world["location"] = "pre Gonandarf Boss Fight"
        return render_template("item_swapped.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], item=item,
                               where=world["location"])
    elif slot == "two":
        world["inventory_two"] = item
        world["location"] = "pre Gonandarf Boss Fight"
        return render_template("item_swapped.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"], item=item,
                               where=world["location"])


@simple_route("/your_turn/<current_monster>/")
def your_turn(world: dict, current_monster: str):
    """
        Handles calculations for the player's turn in battle

        :param world: The current world
        :param current_monster: The monster the player is currently fighting
        :return: The HTML to show the player
        """
    if world["character_current_hp"] <= 0:
        if world["character_current_hp"] < 0:
            world["character_current_hp"] = 0
        return render_template("game_over.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"])
    else:
        return render_template("your_turn.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"],
                               current_monster=current_monster, image=world["monster_image"],
                               height=world["monster_image_height"])


@simple_route("/first_turn/<current_monster>/")
def first_turn(world: dict, current_monster: str):
    """
        Introduces player to battle

        :param world: The current world
        :param current_monster: The monster the player is currently fighting
        :return: The HTML to show the player
        """
    return render_template("first_turn.html", item1=world["inventory_one"],
                           item2=world["inventory_two"], weapon=world["weapon"],
                           current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                           experience=world["character_exp"], level=world["character_lvl"],
                           current_monster=current_monster, image=world["monster_image"],
                           height=world["monster_image_height"])


@simple_route("/battle/<current_monster>/")
def battle(world: dict, current_monster: str):
    """
        Handles both battle victory calculations and monster's turn calculations

        :param world: The current world
        :param current_monster: The monster the player is currently fighting
        :return: The HTML to show the player
        """
    if world["monster_hp"] <= 0:
        if world["location"] == "Gonandarf Boss Fight":
            world["location"] = "endgame"
        elif world["location"] == "Kaleidoscope Boss Fight":
            world["location"] = "forest tunnel"
        elif world["location"] == "Gurg Boss Fight":
            world["location"] = "lake tunnel"
        elif world["location"] == "forest temple":
            world["location"] = "pre Kaleidoscope Boss Fight"
        elif world["location"] == "lake temple":
            world["location"] = "pre Gurg Boss Fight"
        elif world["location"] == "Phantom Gonandarf Boss Fight":
            world["location"] = "post Phantom Gonandarf Boss Fight"
        elif world["location"] == "Merph Boss Fight":
            world["location"] = "post Merph Boss Fight"
        elif world["location"] == "deep forest":
            world["location"] = "pre Phantom Gonandarf Boss Fight"
        elif world["location"] == "lake island":
            world["location"] = "pre Merph Boss Fight"
        elif world["location"] == "left":
            world["location"] = "clearing"
        elif world["location"] == "right":
            world["location"] = "lake"
        world["character_exp"] = world["character_exp"] + world["monster_exp_drop"]
        world["character_current_hp"] = world["character_total_hp"]
        if world["character_exp"] >= 10:
            world["character_lvl"] = world["character_lvl"] + 1
            world["character_exp"] = world["character_exp"] - 10
            world["character_total_hp"] = world["character_total_hp"] + 5
            world["character_current_hp"] = world["character_total_hp"]
            world["character_def"] = world["character_def"] + 1
            return render_template("battle_victory_level_up.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster, exp=world["monster_exp_drop"],
                                   where=world["location"])
        else:
            return render_template("battle_victory.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster, exp=world["monster_exp_drop"],
                                   where=world["location"])
    else:
        atk = world["monster_atk"] - 2
        atk2 = world["monster_atk"] + 1
        damage = random.randrange(atk, atk2)
        world["character_current_hp"] = world["character_current_hp"] - damage
        if world["character_current_hp"] < 0:
            world["character_current_hp"] = 0
        return render_template("monster_turn.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"],
                               current_monster=current_monster, damage=damage, hp=world["character_current_hp"],
                               image=world["monster_image"], height=world["monster_image_height"])


@simple_route("/attack/<current_monster>/")
def attack(world: dict, current_monster: str):
    """
        Handles the player's attacking turn calculations

        :param world: The current world
        :param current_monster: The monster the player is currently fighting
        :return: The HTML to show the player
        """
    damage = 0
    if world["weapon"] == "Sword":
        damage = random.randrange(5, 8)
    elif world["weapon"] == "Super Sword":
        damage = random.randrange(9, 12)
    elif world["weapon"] == "Superer Sword":
        damage = random.randrange(13, 16)
    elif world["weapon"] == "Even Superer Sword":
        damage = random.randrange(17, 20)
    elif world["weapon"] == "Masterful Sword":
        damage = random.randrange(20, 26)
    world["monster_hp"] = world["monster_hp"] - damage
    return render_template("attack.html", item1=world["inventory_one"],
                           item2=world["inventory_two"], weapon=world["weapon"],
                           current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                           experience=world["character_exp"], level=world["character_lvl"],
                           current_monster=current_monster, damage=damage, hp=world["monster_hp"],
                           image=world["monster_image"], height=world["monster_image_height"])


@simple_route("/heal/<current_monster>/")
def heal(world: dict, current_monster: str):
    """
        Handles calculations for player's healing

        :param world: The current world
        :param current_monster: The monster the player is currently fighting
        :return: The HTML to show the player
        """
    if world["character_current_hp"] < world["character_total_hp"]:
        if world["inventory_two"] == "Super Potion":
            world["character_current_hp"] = world["character_current_hp"] + 30
            if world["character_current_hp"] > world["character_total_hp"]:
                world["character_current_hp"] = world["character_total_hp"]
            world["inventory_two"] = "Empty"
            return render_template("heal.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster, hp=30)
        elif world["inventory_one"] == "Super Potion":
            world["character_current_hp"] = world["character_current_hp"] + 30
            if world["character_current_hp"] > world["character_total_hp"]:
                world["character_current_hp"] = world["character_total_hp"]
            world["inventory_one"] = "Empty"
            return render_template("heal.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster, hp=30)
        elif world["inventory_two"] == "Potion":
            world["character_current_hp"] = world["character_current_hp"] + 10
            if world["character_current_hp"] > world["character_total_hp"]:
                world["character_current_hp"] = world["character_total_hp"]
            world["inventory_two"] = "Empty"
            return render_template("heal.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster, hp=10)
        elif world["inventory_one"] == "Potion":
            world["character_current_hp"] = world["character_current_hp"] + 10
            if world["character_current_hp"] > world["character_total_hp"]:
                world["character_current_hp"] = world["character_total_hp"]
            world["inventory_one"] = "Empty"
            return render_template("heal.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster, hp=10)
        else:
            return render_template("heal_fail1.html", item1=world["inventory_one"],
                                   item2=world["inventory_two"], weapon=world["weapon"],
                                   current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                                   experience=world["character_exp"], level=world["character_lvl"],
                                   current_monster=current_monster)
    else:
        return render_template("heal_fail2.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"],
                               current_monster=current_monster)


@simple_route("/flee/<current_monster>/")
def flee(world: dict, current_monster: str):
    """
        Handles player's flee chance

        :param world: The current world
        :param current_monster: The monster that the player is currently fighting
        :return: The HTML to show the player
        """
    flee_chance = random.randrange(1, 11)
    if flee_chance >= 7:
        return render_template("flee_success.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"],
                               current_monster=current_monster)
    else:
        return render_template("flee_fail.html", item1=world["inventory_one"],
                               item2=world["inventory_two"], weapon=world["weapon"],
                               current_hp=world["character_current_hp"], total_hp=world["character_total_hp"],
                               experience=world["character_exp"], level=world["character_lvl"],
                               current_monster=current_monster)


@simple_route("/boss/<where>/")
def boss_fight(world: dict, where: str):
    """
        Handles boss monster creation

        :param world: The current world
        :param where: The current location
        :return: The HTML to show the player
        """
    current_monster = ""
    monster_hp = 0
    monster_atk = 0
    monster_exp_drop = 0
    image = ""
    height = "250"
    if where == "Phantom Gonandarf Boss Fight":
        current_monster = "Phantom Gonandarf"
        monster_hp = 30
        monster_atk = 10
        monster_exp_drop = 15
        image = "https://yt3.ggpht.com/a/AGF-l78c_wi6Yf_hfKWeRI5VvROcL_F5xFX_sVe0mQ=s900-c-k-c0xffffffff-no-rj-mo"
    elif where == "Merph Boss Fight":
        current_monster = "Merph"
        monster_hp = 40
        monster_atk = 8
        monster_exp_drop = 15
        image = "https://i.ytimg.com/vi/D4w63F2XtsE/maxresdefault.jpg"
    elif where == "Kaleidoscope Boss Fight":
        current_monster = "Kaleidoscope"
        monster_hp = 55
        monster_atk = 13
        monster_exp_drop = 17
        image = "https://i5.walmartimages.com/asr/ca282fa3-1645-4416-aad0-1c47b5e623bf_1.57c917d31af8d8d82e7c452b26c4a510.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF"
    elif where == "Gurg Boss Fight":
        current_monster = "Gurg"
        monster_hp = 45
        monster_atk = 15
        monster_exp_drop = 17
        image = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9f41a329-1a82-4f7e-988e-a6aae9322314/d4ll76m-3fb95ba0-b48d-4537-bc07-a18a06d133f2.jpg/v1/fill/w_900,h_675,q_75,strp/derpy_fish_by_banditgirl_d4ll76m-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9Njc1IiwicGF0aCI6IlwvZlwvOWY0MWEzMjktMWE4Mi00ZjdlLTk4OGUtYTZhYWU5MzIyMzE0XC9kNGxsNzZtLTNmYjk1YmEwLWI0OGQtNDUzNy1iYzA3LWExOGEwNmQxMzNmMi5qcGciLCJ3aWR0aCI6Ijw9OTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.3P0DgIxtgqLZ4-65L_eofUPF5HQGH3TKvkpVKXhjRR0"
    elif where == "Gonandarf Boss Fight":
        current_monster = "Gonandarf"
        monster_hp = 60
        monster_atk = 17
        monster_exp_drop = 1
        image = "https://static.tvtropes.org/pmwiki/pub/images/ganon_die.jpg"
    world["monster"] = current_monster
    world["monster_hp"] = monster_hp
    world["monster_atk"] = monster_atk
    world["monster_exp_drop"] = monster_exp_drop
    world["monster_image"] = image
    world["monster_image_height"] = height
    world["location"] = where
    return render_template("boss_fight.html", item1=world["inventory_one"], item2=world["inventory_two"],
                           weapon=world["weapon"], current_hp=world["character_current_hp"],
                           total_hp=world["character_total_hp"], experience=world["character_exp"],
                           level=world["character_lvl"], name=world["monster"], where=where,
                           image=world["monster_image"], height=world["monster_image_height"])


@simple_route("/generate/monster/<where>/")
def generate_monster(world: dict, where: str) -> str:
    """
        Handles random regular monster generation

        :param world: The current world
        :param where: The current location
        :return: The HTML to show the player
        """
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
        monster_exp_drop = 12
        image = "https://66.media.tumblr.com/f927883b6fe0f9547b063f53b02e1428/tumblr_mgs171WwBy1rwcfrqo5_250.jpg"
    elif monster_number == 7:
        current_monster = "Dingdongo"
        monster_hp = 17
        monster_atk = 7
        monster_exp_drop = 10
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
    return render_template("monster.html", item1=world["inventory_one"], item2=world["inventory_two"],
                           weapon=world["weapon"], current_hp=world["character_current_hp"],
                           total_hp=world["character_total_hp"], experience=world["character_exp"],
                           level=world["character_lvl"], name=world["monster"], where=where,
                           image=world["monster_image"], height=world["monster_image_height"])
