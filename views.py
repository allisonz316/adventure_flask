from route_helper import simple_route

GAME_HEADER = """
<h1>Legend of Blah: Blahcarina of Blah</h1>
<p>At any time you can <a href='/reset/'>reset</a> your game.</p>
"""


@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    inventory = "Rope"
    return GAME_HEADER+"""You come across a dark cave.<br>
    You have a {inventory} in your inventory<br>
    
    <a href="goto/cave">Enter the cave.</a><br>
    <a href="goto/entrance">Retreat.</a>"""


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

<!-- Image taken from site that generates random Corgi pictures-->
<img src="http://placecorgi.com/260/180" /><br>
    
What is its name?

<!-- Form allows you to have more text entry -->    
<form action="/save/name/">
    <input type="text" name="player"><br>
    <input type="submit" value="Submit"><br>
</form>
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


@simple_route("/save/name/")
def save_name(world: dict, monsters_name: str) -> str:
    """
    Update the name of the monster.

    :param world: The current world
    :param monsters_name:
    :return:
    """
    world['name'] = monsters_name
    return GAME_HEADER+"""You are in {where}, and you are nearby {monster_name}<br>
    <a href='/'>Return to the start</a>
    """.format(where=world['location'], monster_name=world['name'])
