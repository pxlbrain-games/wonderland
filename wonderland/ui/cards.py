import os
from typing import List

import arcade

from wonderland.ui.ui_element_base import UIElement
from wonderland.config import RESOURCE_PATH
from wonderland.ui.config import FONT


class Card(UIElement):
    """
    Represent a game world entity as a card with image and text content.

    """

    title_color: arcade.arcade_types.Color = arcade.color.BLACK
    title_font: str = FONT

    def __init__(self, title: str, center_x: float = 0.0, center_y: float = 0.0, scale: float = 1.0) -> None:
        super().__init__()
        self.title: str = title
        self._center_x: float = center_x
        self._center_y: float = center_y
        self._scale: float = scale
        self.background: arcade.Sprite = arcade.Sprite(
            filename=os.path.join(RESOURCE_PATH, "card_background.png"),
            scale=self.scale * 0.3,
            center_x=center_x,
            center_y=center_y,
        )
        self.sprite_list: arcade.SpriteList = arcade.SpriteList()
        self.sprite_list.center_x = center_x
        self.sprite_list.center_y = center_y
        self.sprite_list.append(self.background)

    @property
    def center_x(self) -> float:
        return self._center_x

    @center_x.setter
    def center_x(self, value: float) -> None:
        self.sprite_list.move(value - self._center_x, 0.0)
        self._center_x = value

    @property
    def center_y(self) -> float:
        return self._center_y

    @center_y.setter
    def center_y(self, value: float) -> None:
        self.sprite_list.move(0.0, value - self._center_y)
        self._center_y = value

    def draw(self) -> None:
        self.sprite_list.draw()
        arcade.text.draw_text(
            text=self.title,
            color=self.title_color,
            start_x=self.background.center_x - 0.5 * self.background.width,
            start_y=self.background.center_y + 0.5 * self.background.height - 30 * self.scale,
            width=int(self.background.width),
            align="center",
            font_name=self.title_font,
            font_size=int(self.scale * 14),
        )

    @property
    def scale(self) -> float:
        return self._scale

    @scale.setter
    def scale(self, value: float) -> None:
        self.background.scale *= value / self._scale
        self._scale = value


class CardRow(UIElement):
    """
    Row up cards and interact with them via mouse

    """

    highlight_scale: float = 1.6

    def __init__(self, center_x: float, center_y: float, width: float, cards: List[Card] = None) -> None:
        self.center_x: float = center_x
        self.center_y: float = center_y
        self.width: float = width
        self._cards: List[Card] = list() if cards is None else cards
        self.highlighted_card: Card = None

    def _arrange_cards(self) -> None:
        for i, card in enumerate(reversed(self._cards)):
            card.center_x = self.center_x + self.width * (i / (len(self._cards) - 1) - 0.5)
            card.center_y = self.center_y
            card.scale = 1.0
            if self.highlighted_card is card:
                card.scale = self.highlight_scale
                card.center_y += card.background.height * 0.2

    def append(self, card: Card) -> None:
        self._cards.append(card)

    def draw(self) -> None:
        self._arrange_cards()
        for card in self._cards:
            if card is not self.highlighted_card:
                card.draw()
        # The highlighted card should be drawn above all others
        if self.highlighted_card is not None:
            self.highlighted_card.draw()

    def on_mouse_motion(self, x: float, y: float) -> None:
        card_collision = False
        for card in self._cards:
            if card.background.collides_with_point((x, y)):
                card_collision = True
                self.highlighted_card = card
        if not card_collision:
            if self.highlighted_card:
                self.highlighted_card = None
