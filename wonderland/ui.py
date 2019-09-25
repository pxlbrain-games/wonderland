import os

import arcade

RESOURCE_PATH: str = os.path.join(os.path.dirname(__file__), "resources")

FONT: str = "Gabriola"

class CardRow:
    """
    Row up cards and interact with them via mouse

    """

    def __init__(self, cards: list = None):
        self.cards = list() if cards is None else cards
        self.highlighted_card = None

    def draw(self):
        for card in self.cards:
            if card is not self.highlighted_card:
                card.draw()
        if self.highlighted_card:
            self.highlighted_card.draw()

    def on_mouse_motion(self, x, y):
        card_collision = False
        for card in self.cards:
            if card.background.collides_with_point((x, y)):
                card_collision = True
                if self.highlighted_card:
                    self.highlighted_card.scale = 1.0
                self.highlighted_card = card
                card.scale = 1.6
        if not card_collision:
            if self.highlighted_card:
                self.highlighted_card.scale = 1.0
                self.highlighted_card = None

class Card(arcade.SpriteList):
    """
    Represent a game world entity as a card with image and text content.

    """

    background_color: arcade.arcade_types.Color = arcade.color.DARK_CERULEAN
    shadow_color: arcade.arcade_types.Color = arcade.color.BLACK
    title_color: arcade.arcade_types.Color = arcade.color.BLACK
    title_font: str = FONT

    def __init__(self, title: str, center_x: float, center_y: float):
        super().__init__()
        self.title = title
        self.center_x = center_x
        self.center_y = center_y
        self._scale = 1.0
        self.background = arcade.Sprite(
            filename=os.path.join(RESOURCE_PATH, "card_background.png"),
            scale=self.scale * 0.3,
            center_x=center_x,
            center_y=center_y,
        )
        self.append(self.background)

    def draw(self):
        super().draw()
        arcade.text.draw_text(
            text=self.title,
            color=self.title_color,
            start_x=self.center_x-0.5*self.background.width,
            start_y=self.center_y+0.5*self.background.height-30*self.scale,
            width=int(self.background.width),
            align="center",
            font_name=self.title_font,
            font_size=int(self.scale*14)
        )

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        self.background.scale *= value/self._scale
        self._scale = value
