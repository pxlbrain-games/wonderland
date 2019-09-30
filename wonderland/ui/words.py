import random
from typing import List

import arcade

from wonderland.ui.ui_element_base import UIElement, UIContainer, Clickable, Hoverable, Rectangle
from wonderland.ui.config import FONT


class Word(UIElement, Rectangle, Clickable, Hoverable):
    """
    Display a word on the screen

    """

    text_color: arcade.arcade_types.Color = arcade.color.ALICE_BLUE
    font_size: int = 15

    def __init__(self, text: str, center_x: float = 0.0, center_y: float = 0.0):
        self.text: str = text
        self.center_x = center_x
        self.center_y = center_y
        self.scale: float = 1.0

    @Rectangle.width.getter  # type: ignore
    def width(self) -> float:
        return len(self.text) * self.scale * self.font_size * 0.5

    @Rectangle.height.getter  # type: ignore
    def height(self) -> float:
        return self.scale * self.font_size * 1.25

    def draw(self) -> None:
        arcade.text.draw_text(
            text=self.text,
            start_x=self.center_x,
            start_y=self.center_y,
            color=self.text_color,
            font_name=FONT,
            font_size=int(self.scale * self.font_size),
            anchor_x="center",
            anchor_y="center",
        )

    def on_click(self) -> None:
        pass

    def on_hover(self) -> None:
        pass

    def on_hover_end(self) -> None:
        pass


class WordCloud(UIContainer):
    """
    Arrange words in an interactive word cloud

    """

    highlight_scale: float = 2.0

    def __init__(
        self, center_x: float, center_y: float, width: float, height: float, words: List[Word] = None
    ) -> None:
        self.center_x: float = center_x
        self.center_y: float = center_y
        self.width: float = width
        self.height: float = height
        self._words: List[Word] = list()
        if words is not None:
            map(self.append, words)
        self._arrange_words()

    @classmethod
    def _word_on_hover(cls, word: Word):
        word.scale = cls.highlight_scale

    @staticmethod
    def _word_on_hover_end(word: Word):
        word.scale = 1.0

    def _arrange_words(self) -> None:
        for word in self._words:
            word.center_x = self.center_x + (random.random() - 0.5) * self.width
            word.center_y = self.center_y + (random.random() - 0.5) * self.height

    def append(self, word: Word) -> None:
        word.on_hover = lambda: self._word_on_hover(word)
        word.on_hover_end = lambda: self._word_on_hover_end(word)
        self._words.append(word)
        self.ui_elements.append(word)
        self._arrange_words()
