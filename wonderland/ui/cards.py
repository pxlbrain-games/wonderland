import os
from typing import List
from enum import Enum

import arcade

from wonderland.ui.ui_element_base import UIElement, UIContainer, Clickable, Hoverable, Rectangle
from wonderland.config import RESOURCE_PATH
from wonderland.ui.config import FONT


class CardType(Enum):
    CHARACTER = 1
    PLACE = 2
    THING = 3


CARD_TYPE_ICONS = {
    CardType.CHARACTER: os.path.join(RESOURCE_PATH, "icons/lorc/sensuousness.png"),
    CardType.PLACE: os.path.join(RESOURCE_PATH, "icons/lorc/treasure-map.png"),
    CardType.THING: os.path.join(RESOURCE_PATH, "icons/lorc/hand.png"),
}


class Card(UIElement, Rectangle, Clickable, Hoverable):
    """
    Represent a game world entity as a card with image and text content.

    """

    title_color: arcade.arcade_types.Color = arcade.color.BLACK
    title_font: str = FONT

    def __init__(
        self,
        card_type: CardType,
        title: str,
        subtitle: str = "",
        center_x: float = 0.0,
        center_y: float = 0.0,
        scale: float = 1.0,
    ) -> None:
        self._card_type = card_type
        self.title: str = title
        self.subtitle: str = subtitle
        self._center_x: float = center_x
        self._center_y: float = center_y
        self._scale: float = scale
        self.background: arcade.Sprite = arcade.Sprite(
            filename=os.path.join(RESOURCE_PATH, "card_background.png"),
            scale=self.scale * 0.3,
            center_x=center_x,
            center_y=center_y,
        )
        self.type_icon: arcade.Sprite = arcade.Sprite(
            filename=CARD_TYPE_ICONS[card_type],
            scale=self.scale * 0.04,
            center_x=center_x - self.background.width / 2 + self.scale * 22,
            center_y=center_y + self.background.height / 2 - self.scale * 24,
        )
        self.type_icon.alpha = 190
        self.sprite_list: arcade.SpriteList = arcade.SpriteList()
        self.sprite_list.center_x = center_x
        self.sprite_list.center_y = center_y
        self.sprite_list.append(self.background)
        self.sprite_list.append(self.type_icon)

    @property
    def card_type(self) -> CardType:
        return self._card_type

    @card_type.setter
    def card_type(self, value: CardType) -> None:
        self._card_type = value
        self.type_icon.kill()
        self.type_icon = arcade.Sprite(
            filename=CARD_TYPE_ICONS[self._card_type],
            scale=self.scale * 0.04,
            center_x=self.center_x - self.background.width / 2 + self.scale * 22,
            center_y=self.center_y + self.background.height / 2 - self.scale * 24,
        )
        self.type_icon.alpha = 190
        self.sprite_list.append(self.type_icon)

    @Rectangle.center_x.setter  # type: ignore
    def center_x(self, value: float) -> None:
        self.sprite_list.move(value - self._center_x, 0.0)
        self._center_x = value

    @Rectangle.center_y.setter  # type: ignore
    def center_y(self, value: float) -> None:
        self.sprite_list.move(0.0, value - self._center_y)
        self._center_y = value

    @Rectangle.height.getter  # type: ignore
    def height(self) -> float:
        return self.background.height

    @Rectangle.width.getter  # type: ignore
    def width(self) -> float:
        return self.background.width

    @property
    def scale(self) -> float:
        return self._scale

    @scale.setter
    def scale(self, value: float) -> None:
        factor = value / self._scale
        for sprite in self.sprite_list:
            sprite.center_x = (sprite.center_x - self.center_x) * factor + self.center_x
            sprite.center_y = (sprite.center_y - self.center_y) * factor + self.center_y
            sprite.scale *= factor
        self._scale = value

    def draw(self) -> None:
        self.sprite_list.draw()
        arcade.draw_text(
            text=self.title,
            color=self.title_color,
            start_x=self.center_x - 0.5 * self.width,
            start_y=self.center_y + 0.5 * self.height - 30 * self.scale,
            width=int(self.width),
            align="center",
            font_name=self.title_font,
            font_size=int(self.scale * 14),
        )
        arcade.draw_text(
            text="~ " + self.subtitle + " ~",
            color=self.title_color,
            start_x=self.center_x - 0.5 * self.width,
            start_y=self.center_y + 0.5 * self.height - 42 * self.scale,
            width=int(self.width),
            align="center",
            font_name=self.title_font,
            font_size=int(self.scale * 10),
            italic=True,
        )

    def collides_with_point(self, point: arcade.arcade_types.Point) -> bool:
        return self.background.collides_with_point(point)

    def on_click(self) -> None:
        pass

    def on_hover(self) -> None:
        pass

    def on_hover_end(self) -> None:
        pass


class CardRow(UIContainer):
    """
    Row up cards and interact with them via mouse.

    """

    highlight_scale: float = 1.6

    def __init__(self, center_x: float, center_y: float, width: float, cards: List[Card] = None) -> None:
        self.center_x: float = center_x
        self.center_y: float = center_y
        self.width: float = width
        self._cards: List[Card] = list()
        if cards is not None:
            map(self.append, cards)
        self._arrange_cards()

    def _card_on_hover(self, card: Card):
        card.scale = self.highlight_scale
        card.center_y = self.center_y + card.height * 0.2
        card.z_value = 1.0

    def _card_on_hover_end(self, card: Card):
        card.scale = 1.0
        card.center_y = self.center_y
        card.z_value = 0.0

    def _arrange_cards(self) -> None:
        for i, card in enumerate(reversed(self._cards)):
            card.center_x = (
                self.center_x + self.width * (i / (len(self._cards) - 1) - 0.5)
                if len(self._cards) > 1
                else self.center_x
            )
            card.center_y = self.center_y

    def append(self, card: Card) -> None:
        card.on_hover = lambda: self._card_on_hover(card)
        card.on_hover_end = lambda: self._card_on_hover_end(card)
        self._cards.append(card)
        self.ui_elements.append(card)
        self._arrange_cards()
