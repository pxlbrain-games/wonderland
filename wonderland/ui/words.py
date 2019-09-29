import random
from typing import List

import arcade

from wonderland.ui.ui_element_base import UIElement
from wonderland.ui.config import FONT


class Word(UIElement):
    """
    Display a word on the screen

    """

    text_color: arcade.arcade_types.Color = arcade.color.ALICE_BLUE

    def __init__(self, text: str, center_x: float = 0.0, center_y: float = 0.0):
        self.text: str = text
        self.center_x: float = center_x
        self.center_y: float = center_y
        self.scale: float = 1.0

    @property
    def width(self) -> float:
        return len(self.text) * self.scale * 15

    @property
    def height(self) -> float:
        return self.scale * 20

    def collides_with_point(self, point: arcade.arcade_types.Point) -> bool:
        return (self.center_x - self.width / 2 < point[0] < self.center_x + self.width / 2) and (
            self.center_y - self.height / 2 < point[1] < self.center_y + self.height / 2
        )

    def draw(self) -> None:
        arcade.text.draw_text(
            text=self.text,
            start_x=self.center_x,
            start_y=self.center_y,
            color=self.text_color,
            font_name=FONT,
            font_size=int(self.scale * 15),
            anchor_x="center",
        )


class WordCloud(UIElement):
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
        self._words: List[Word] = list() if words is None else words
        self._arrange_words()
        self.highlighted_word: Word = None

    def _arrange_words(self) -> None:
        for word in self._words:
            word.center_x = self.center_x + (random.random() - 0.5) * self.width
            word.center_y = self.center_y + (random.random() - 0.5) * self.height

    def append(self, word: Word) -> None:
        self._words.append(word)
        self._arrange_words()

    def on_mouse_motion(self, x: float, y: float) -> None:
        word_collision = False
        for word in self._words:
            if word.collides_with_point((x, y)):
                word_collision = True
                if self.highlighted_word is not word:
                    if self.highlighted_word is not None:
                        self.highlighted_word.scale = 1.0
                    word.scale = self.highlight_scale
                    self.highlighted_word = word
        if not word_collision and self.highlighted_word is not None:
            self.highlighted_word.scale = 1.0
            self.highlighted_word = None

    def draw(self) -> None:
        for word in self._words:
            word.draw()
