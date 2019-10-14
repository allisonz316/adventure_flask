from route_helper import simple_route

inventory = ["Rope", "Lantern", "Potion"]
weapons = "Sword"

GAME_HEADER = """
<h1>Legend of Zolda: Parody of Time</h1>
Your Inventory: {item1}, {item2}, {item3}<br>
Your Weapon: {weapon}<p>
""".format(item1=inventory[0], item2=inventory[1], item3=inventory[2], weapon=weapons)


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
    
<a href="/goto/left/">Left path</a><br>
<a href="/goto/right/">Right path</a>
    
"""

GONE_LEFT = """
You have gone left<p>
<a href='/'>Return to the start</a>
"""

GONE_RIGHT = """
You have gone right<p>
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
    if where == "forest":
        return GAME_HEADER+FOREST_ENTER
    elif where == "give_up":
        return GAME_HEADER+GIVE_UP
    elif where == "left":
        return GAME_HEADER+GONE_LEFT
    elif where == "right":
        return GAME_HEADER+GONE_RIGHT
