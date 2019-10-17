from route_helper import simple_route
from route_helper import INITIAL_WORLD
import random
from PIL import Image

GAME_HEADER = """
<h1>Legend of Zolda: Majora's Flask</h1>
HP: {current_hp}/{total_hp}<br>
Level: {level}<br>
EXP: {experience}<p>
Inventory:<br>
........Slot One: {item1}<br>
........Slot Two: {item2}<br>
........Slot Three: {item3}<br>
........Slot Four: {item4}<p>
Weapon: {weapon}<p>
************<p>
""".format(item1=INITIAL_WORLD["inventory_slot_one"], item2=INITIAL_WORLD["inventory_slot_two"],
           item3=INITIAL_WORLD["inventory_slot_three"], item4=INITIAL_WORLD["inventory_slot_four"],
           weapon=INITIAL_WORLD["weapons"], current_hp=INITIAL_WORLD["current_hp"], total_hp=INITIAL_WORLD["total_hp"],
           experience=INITIAL_WORLD["exp"], level=INITIAL_WORLD["lvl"])


@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """

    return GAME_HEADER+"""Your name is Lonk, a completely original fantasy hero on a quest to save Zolda, a completely 
    original fantasy princess, from Gonandarf, a completely original fantasy villain. Your completely original fantasy 
    travels have first brought you to the edge of a dark, spooky forest.<p>
    What will you do?<p>
    <img src="https://wallpaperaccess.com/full/96689.jpg"
    width="350" height="250"/><br>
    <a href="goto/forest">Enter the forest</a><br>
    <a href="goto/give_up">Give up</a>
    """


GIVE_UP = """
You've...given up. Uh...okay. Not really sure why you decided to do that...but...I guess we're done here, then.<p>
...bye.<p>
<a href = "/">Retry?</a>
"""

FOREST_ENTER = """
Upon entering the forest, you see two paths in front of you.<p>
    
Where will you go?<p>
    
<a href="/generate/monster/left/">Left path</a><br>
<a href="/generate/monster/right/">Right path</a>
    
"""


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
        return GAME_HEADER+FOREST_ENTER
    elif where == "give_up":
        return GAME_HEADER+GIVE_UP


@simple_route("/first_turn/<current_monster>/")
def first_turn(world: dict, current_monster: dict):
    return GAME_HEADER + """
    You approach the {current_monster}.<p>
    What will you do?<p>
    <a href="/attack/">Attack</a><br>
    <a href="/heal/">Heal</a><br>
    <a href="/flee/">Flee</a><br>
    """.format(current_monster=current_monster)


@simple_route("/battle/<current_monster>/")
def battle(world: dict, current_monster: dict):
    pass


@simple_route("/attack/")
def attack(world: dict, current_monster: dict):
    damage = 0
    if INITIAL_WORLD["weapons"] == "sword":
        damage = random.randrange(4, 7)
        damage = damage - (current_monster["def"]/2)
    return damage


@simple_route("/heal/")
def heal(world: dict):
    if INITIAL_WORLD["inventory_slot_one"] == "Potion":
        INITIAL_WORLD["current_hp"] = INITIAL_WORLD["current_hp"] + 10
        INITIAL_WORLD["inventory_slot_one"] = "Empty"
        return GAME_HEADER + """Healed 10 HP!
                <a href="/goto/forest/">Enter the forest</a><br>
        """
    else:
        return GAME_HEADER + """Couldn't heal!
                <a href="/goto/forest/">Enter the forest</a><br>
        """


@simple_route("/flee/")
def flee(world: dict):
    flee_chance = random.randrange(1, 11)
    if flee_chance >= 7:
        return GAME_HEADER + """Successfully fled!<br>
                <a href="/goto/forest/">Enter the forest</a><br>
        """
    else:
        return GAME_HEADER + """Couldn't flee!
                <a href="/goto/forest/">Enter the forest</a><br>
        """


@simple_route("/generate/monster/<where>/")
def generate_monster(world: dict, where: str) -> str:
    monster_number = random.randrange(1, 10)
    current_monster = {}
    if monster_number == 1:
        current_monster = {"name": "Gel-O", "hp": 7, "atk": 4, "def": 1, "exp_drop": 3}
    elif monster_number == 2:
        current_monster = {"name": "Beehat", "hp": 12, "atk": 6, "def": 3, "exp_drop": 5}
    elif monster_number == 3:
        current_monster = {"name": "Socktorok", "hp": 15, "atk": 5, "def": 4, "exp_drop": 6}
    elif monster_number == 4:
        current_monster = {"name": "Beever", "hp": 8, "atk": 3, "def": 2, "exp_drop": 4}
    elif monster_number == 5:
        current_monster = {"name": "Dinofloss", "hp": 14, "atk": 7, "def": 4, "exp_drop": 8}
    elif monster_number == 6:
        current_monster = {"name": "Wolfy", "hp": 18, "atk": 8, "def": 5, "exp_drop": 10}
    elif monster_number == 7:
        current_monster = {"name": "Dingdongo", "hp": 17, "atk": 7, "def": 9, "exp_drop": 12}
    elif monster_number == 8:
        current_monster = {"name": "Key", "hp": 6, "atk": 3, "def": 1, "exp_drop": 2}
    elif monster_number == 9:
        current_monster = {"name": "Wizzo", "hp": 10, "atk": 7, "def": 3, "exp_drop": 8}
    world['monster'] = current_monster
    world['location'] = where
    if where == "left":
        if monster_number == 1:
            return GAME_HEADER + """You have gone left and found a {name}.<p>
                               <img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/95c81da5-abd3-499e-bb71-a32be4435115/d38yzcn-be11f801-06e2-4d96-bd13-483c1493b971.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzk1YzgxZGE1LWFiZDMtNDk5ZS1iYjcxLWEzMmJlNDQzNTExNVwvZDM4eXpjbi1iZTExZjgwMS0wNmUyLTRkOTYtYmQxMy00ODNjMTQ5M2I5NzEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.6yDXL-r4fgQwWe3JJk2z5jxZAk0NVIDEPy2VD-hUZhw"
                               width="300" height="250"/><br>
                               What will you do?<p>
                               <a href="/first_turn/{name}/">Engage in Battle</a><br>
                               <a href="/flee/">Try to Run</a><br>
                               """.format(name=current_monster["name"])
        elif monster_number == 2:
            return GAME_HEADER + """You have gone left and found a {name}.<p>
                                           <img src="https://images4-g.ravelrycache.com/uploads/LuckyFoxKnits/549000002/Second_cover_small2.jpg"
                                           width="300" height="250"/><br>
                                           What will you do?<p>
                                           <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                           <a href="/flee/">Try to Run</a><br>
                                           """.format(name=current_monster["name"])
        elif monster_number == 3:
            return GAME_HEADER + """You have gone left and found a {name}.<p>
                                           <img src="https://images4-g.ravelrycache.com/uploads/kjbrasda/244331547/DSCF7897_small2.JPG"
                                           width="300" height="250"/><br>
                                           What will you do?<p>
                                           <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                           <a href="/flee/">Try to Run</a><br>
                                           """.format(name=current_monster["name"])
        elif monster_number == 4:
            return GAME_HEADER + """You have gone left and found a {name}.<p>
                                                       <img src="https://img.huffingtonpost.com/asset/5cd6f6ee2100005800c86c95.jpeg?ops=scalefit_630_noupscale"
                                                       width="300" height="300"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])
        elif monster_number == 5:
            return GAME_HEADER + """You have gone left and found a {name}.<p>
                                                       <img src="https://images-na.ssl-images-amazon.com/images/I/51T0TWGJYQL._SY355_.jpg"
                                                       width="300" height="250"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])
        elif monster_number == 6:
            return GAME_HEADER + """You have gone left and found a {name}.<p>
                                                       <img src="https://66.media.tumblr.com/f927883b6fe0f9547b063f53b02e1428/tumblr_mgs171WwBy1rwcfrqo5_250.jpg"
                                                       width="300" height="250"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])
        elif monster_number == 7:
            return GAME_HEADER + """You have gone left and found a {name}.<p>
                                                       <img src="https://images-na.ssl-images-amazon.com/images/I/51QnDuSzMqL.jpg"
                                                       width="300" height="250"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])
        elif monster_number == 8:
            return GAME_HEADER + """You have gone left and found a {name}.<p>
                                                       <img src="https://vignette.wikia.nocookie.net/clubpenguin/images/e/ea/7126_icon.png/revision/latest?cb=20121004074608"
                                                       width="300" height="250"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])
        elif monster_number == 9:
            return GAME_HEADER + """You have gone left and found a {name}.<p>
                                                       <img src="https://www.how-to-draw-funny-cartoons.com/images/wizard-clipart-004.png"
                                                       width="300" height="300"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])
    elif where == "right":
        if monster_number == 1:
            return GAME_HEADER + """You have gone right and found a {name}.<p>
                               <img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/95c81da5-abd3-499e-bb71-a32be4435115/d38yzcn-be11f801-06e2-4d96-bd13-483c1493b971.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzk1YzgxZGE1LWFiZDMtNDk5ZS1iYjcxLWEzMmJlNDQzNTExNVwvZDM4eXpjbi1iZTExZjgwMS0wNmUyLTRkOTYtYmQxMy00ODNjMTQ5M2I5NzEucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.6yDXL-r4fgQwWe3JJk2z5jxZAk0NVIDEPy2VD-hUZhw"
                               width="300" height="250"/><br>
                               What will you do?<p>
                               <a href="/first_turn/{name}/">Engage in Battle</a><br>
                               <a href="/flee/">Try to Run</a><br>
                               """.format(name=current_monster["name"])
        elif monster_number == 2:
            return GAME_HEADER + """You have gone right and found a {name}.<p>
                                           <img src="https://images4-g.ravelrycache.com/uploads/LuckyFoxKnits/549000002/Second_cover_small2.jpg"
                                           width="300" height="250"/><br>
                                           What will you do?<p>
                                           <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                           <a href="/flee/">Try to Run</a><br>
                                           """.format(name=current_monster["name"])
        elif monster_number == 3:
            return GAME_HEADER + """You have gone right and found a {name}.<p>
                                           <img src="https://images4-g.ravelrycache.com/uploads/kjbrasda/244331547/DSCF7897_small2.JPG"
                                           width="300" height="250"/><br>
                                           What will you do?<p>
                                           <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                           <a href="/flee/">Try to Run</a><br>
                                           """.format(name=current_monster["name"])
        elif monster_number == 4:
            return GAME_HEADER + """You have gone right and found a {name}.<p>
                                                       <img src="https://img.huffingtonpost.com/asset/5cd6f6ee2100005800c86c95.jpeg?ops=scalefit_630_noupscale"
                                                       width="300" height="300"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])
        elif monster_number == 5:
            return GAME_HEADER + """You have gone right and found a {name}.<p>
                                                       <img src="https://images-na.ssl-images-amazon.com/images/I/51T0TWGJYQL._SY355_.jpg"
                                                       width="300" height="250"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])
        elif monster_number == 6:
            return GAME_HEADER + """You have gone right and found a {name}.<p>
                                                       <img src="https://66.media.tumblr.com/f927883b6fe0f9547b063f53b02e1428/tumblr_mgs171WwBy1rwcfrqo5_250.jpg"
                                                       width="300" height="250"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])
        elif monster_number == 7:
            return GAME_HEADER + """You have gone right and found a {name}.<p>
                                                       <img src="https://images-na.ssl-images-amazon.com/images/I/51QnDuSzMqL.jpg"
                                                       width="300" height="250"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])
        elif monster_number == 8:
            return GAME_HEADER + """You have gone right and found a {name}.<p>
                                                       <img src="https://vignette.wikia.nocookie.net/clubpenguin/images/e/ea/7126_icon.png/revision/latest?cb=20121004074608"
                                                       width="300" height="250"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])
        elif monster_number == 9:
            return GAME_HEADER + """You have gone right and found a {name}.<p>
                                                       <img src="https://www.how-to-draw-funny-cartoons.com/images/wizard-clipart-004.png"
                                                       width="300" height="300"/><br>
                                                       What will you do?<p>
                                                       <a href="/first_turn/{name}/">Engage in Battle</a><br>
                                                       <a href="/flee/">Try to Run</a><br>
                                                       """.format(name=current_monster["name"])