from wonderland.screens.screen_base import Screen
from wonderland.ui import Card


class CardCreator(Screen):
    """
    Create a Wonderland playing card.

    """

    def __init__(self):
        self.card: Card = None

    def setup(self, width: int, height: int) -> None:
        self.card = Card(title="Untitled", center_x=width / 2, center_y=height / 2, scale=3.0)

    def draw(self) -> None:
        self.card.draw()

    def on_mouse_motion(self, x: float, y: float) -> None:
        pass
