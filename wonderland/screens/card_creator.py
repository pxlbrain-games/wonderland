from wonderland.screens.screen_base import Screen
from wonderland.ui import Card, Button


class CardCreator(Screen):
    """
    Create a Wonderland playing card.

    """

    def __init__(self) -> None:
        self.card: Card = None
        self.button: Button = None

    def setup(self, width: int, height: int) -> None:
        self.card = Card(title="Untitled", center_x=width / 2, center_y=height / 2, scale=3.0)
        self.button = Button(
            text="Click Me", center_x=width / 6, center_y=height * 0.8, scale=2.0, on_click=lambda: print("Hello")
        )
        self.ui_elements.append(self.card)
        self.ui_elements.append(self.button)

    def update(self, time_delta: float) -> None:
        pass
