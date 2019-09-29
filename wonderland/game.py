from typing import Dict

import arcade

from wonderland.screens import Screen, Scene, CardCreator

SCREEN_TITLE = "Wonderland Prototype"


class Wonderland(arcade.Window):
    """
    Main application class of the Wonderland prototype.
    """

    def __init__(self, width, height, title=SCREEN_TITLE):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.screens: Dict[str, Screen] = {"scene": Scene(), "card_creator": CardCreator()}
        self.current_screen: Screen = self.screens["card_creator"]

    @property
    def width(self) -> int:
        return self.get_size()[0]

    @property
    def height(self) -> int:
        return self.get_size()[1]

    def setup(self) -> None:
        # Create your sprites and sprite lists here
        for screen in self.screens.values():
            screen.setup(self.width, self.height)

    def on_draw(self) -> None:
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.current_screen.draw()

    def update(self, delta_time: float) -> None:
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.ENTER:
            if self.current_screen is self.screens["scene"]:
                self.current_screen = self.screens["card_creator"]
            else:
                self.current_screen = self.screens["scene"]

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.current_screen.on_mouse_motion(x, y)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass
