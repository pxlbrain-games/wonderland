import arcade

from wonderland.ui import Card, CardRow, Word, WordCloud

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Wonderland Prototype"


class Wonderland(arcade.Window):
    """
    Main application class of the Wonderland prototype.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.card_row: CardRow = None
        self.word_cloud: WordCloud = None

    def setup(self):
        # Create your sprites and sprite lists here
        self.word_cloud = WordCloud(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.8, SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.2)
        for _ in range(5):
            self.word_cloud.append(Word("Hello"))
        self.card_row = CardRow(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.2, SCREEN_WIDTH * 0.7)
        for _ in range(4):
            self.card_row.append(Card("Foobar"))

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.word_cloud.draw()
        self.card_row.draw()

    def update(self, delta_time):
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
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.card_row.on_mouse_motion(x, y)
        self.word_cloud.on_mouse_motion(x, y)

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


game = Wonderland(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
