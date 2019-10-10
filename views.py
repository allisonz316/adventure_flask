from route_helper import simple_route

inventory = ["Rope", "Lantern", "Potion"]
weapons = "Sword"

GAME_HEADER = """
<h1>Legend of Blah: Blahcarina of Blah</h1>
<p>Your Inventory: {item1}, {item2}, {item3}</p>
<o>Your Weapon: {weapon}</p>
""".format(item1=inventory[0], item2=inventory[1], item3=inventory[2], weapon = weapons)


@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """

    return GAME_HEADER+"""You come across a dark cave.<br>
    <a href="goto/cave">Enter the cave</a><br>
    """


CAVE_ENTER = """
Upon entering the cave, you see two paths in front of you.<br>
    
Where will you go?<br>
    
<a href="/goto/left/">Left path</a><br>
<a href="/goto/right/">Right path</a>
    
"""

GONE_LEFT = """
You have gone left<br>
<a href='/'>Return to the start</a>
"""

GONE_RIGHT = """
You have gone right<br>
<a href='/'>Return to the start</a>
"""

ENCOUNTER_MONSTER = """
<!-- Curly braces let us inject values into the string -->
You are in {}. You found a monster!<br>

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
    if where == "cave":
        return GAME_HEADER+CAVE_ENTER
    elif where == "left":
        return GAME_HEADER+GONE_LEFT
    elif where == "right":
        return GAME_HEADER+GONE_RIGHT

