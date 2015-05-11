# coding=utf-8
"""
Demo story.

'Tale' mud driver, mudlib and interactive fiction framework
Copyright by Irmen de Jong (irmen@razorvine.net)
"""
from __future__ import absolute_import, print_function, division, unicode_literals
import datetime
import sys
from tale.hints import Hint
from tale.driver import StoryConfig
from tale.main import run_story


class Story(object):
    config = StoryConfig(
        name="Tale Demo",
        author="Irmen de Jong",
        author_address="irmen@razorvine.net",
        version="1.2",                  # arbitrary but is used to check savegames for compatibility
        requires_tale="2.0",            # tale library required to run the game
        supported_modes={"if", "mud"},  # what driver modes (if/mud) are supported by this story
        player_name=None,               # set a name to create a prebuilt player, None to use the character builder
        player_gender=None,             # m/f/n
        player_race=None,               # default is "human" of course, but you can select something else if you want
        money_type="modern",            # money type modern/fantasy/None
        server_tick_method="timer",     # 'command' (waits for player entry) or 'timer' (async timer driven)
        server_tick_time=1.0,           # time between server ticks (in seconds) (usually 1.0 for 'timer' tick method)
        gametime_to_realtime=5,         # meaning: game time is X times the speed of real time (only used with "timer" tick method)
        max_wait_hours=2,               # the max. number of hours (game time) the player is allowed to wait
        display_gametime=True,          # enable/disable display of the game time at certain moments
        epoch=datetime.datetime(2012, 4, 19, 14, 0, 0),    # start date/time of the game clock
        startlocation_player="town.square",
        startlocation_wizard="wizardtower.hall",
        savegames_enabled=True,
        license_file="messages/license.txt"
    )

    driver = None     # will be set by driver init()

    def init(self, driver):
        """Called by the game driver when it is done with its initial initialization"""
        self.driver = driver

    def init_player(self, player):
        """
        Called by the game driver when it has created the player object.
        You can set the hint texts on the player object, or change the state object, etc.
        """
        player.hints.init([
            Hint(None, None, "Find a way to open the door that leads to the exit of the game."),
            Hint("unlocked_enddoor", None, "Step out through the door into the freedom!")
        ])

    def welcome(self, player):
        """welcome text when player enters a new game"""
        player.tell("<bright>Welcome to %s.</>" % self.config.name, end=True)
        player.tell("\n")
        player.tell(self.driver.resources["messages/welcome.txt"].data)
        player.tell("\n")

    def welcome_savegame(self, player):
        """welcome text when player enters the game after loading a saved game"""
        player.tell("<bright>Welcome back to %s.</>" % self.config.name, end=True)
        player.tell("\n")
        player.tell(self.driver.resources["messages/welcome.txt"].data)
        player.tell("\n")

    def goodbye(self, player):
        """goodbye text when player quits the game"""
        player.tell("Goodbye, %s. Please come back again soon." % player.title)
        player.tell("\n")

    def completion(self, player):
        """congratulation text / finale when player finished the game (story_complete event)"""
        player.tell("<bright>Congratulations! You've finished the game!</>")


if __name__ == "__main__":
    # story is invoked as a script, start it in the Tale Driver.
    run_story(sys.path[0])
