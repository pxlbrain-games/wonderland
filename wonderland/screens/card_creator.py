from typing import List, Optional

from wonderland.screens.screen_base import Screen
from wonderland.ui import Card, CardType, Button, ButtonChooser


class CardCreator(Screen):
    """
    Create a Wonderland playing card.

    """

    def __init__(self) -> None:
        self.card: Optional[Card] = None
        self.card_type_chooser: Optional[ButtonChooser] = None

    def setup(self, width: int, height: int) -> None:
        self.card = Card(
            card_type=CardType.CHARACTER,
            title="Untitled",
            subtitle="Card",
            center_x=width / 2,
            center_y=height / 2,
            scale=3.0,
        )
        self.ui_elements.append(self.card)
        self.card_type_chooser = ButtonChooser(
            options={
                "Character": [CardType.CHARACTER, "Alice"],
                "Place": [CardType.PLACE, "The Dark Forest"],
                "Thing": [CardType.THING, "The Gemstone"],
            },
            center_x=width / 6,
            center_y=height * 0.9,
            width=300,
            on_choice=self.on_card_type_choice,
            on_choice_reset=lambda: setattr(self.card, "title", "Untitled"),
        )
        self.ui_elements.append(self.card_type_chooser)

    def on_card_type_choice(self, option):
        self.card.title = option[1]
        self.card.card_type = option[0]

    def update(self, time_delta: float) -> None:
        pass
