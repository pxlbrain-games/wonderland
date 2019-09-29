import random

import arcade

from wonderland.ui.config import FONT


class Word:
    """
    Display a word on the screen

    """

    text_color: arcade.arcade_types.Color = arcade.color.ALICE_BLUE

    def __init__(self, text: str, center_x: float = 0.0, center_y: float = 0.0):
        self.text = text
        self.center_x = center_x
        self.center_y = center_y
        self.scale = 1.0

    @property
    def width(self):
        return len(self.text) * self.scale * 15

    @property
    def height(self):
        return self.scale * 20

    def collides_with_point(self, point):
        return (self.center_x - self.width / 2 < point[0] < self.center_x + self.width / 2) and (
            self.center_y - self.height / 2 < point[1] < self.center_y + self.height / 2
        )

    def draw(self):
        arcade.text.draw_text(
            text=self.text,
            start_x=self.center_x,
            start_y=self.center_y,
            color=self.text_color,
            font_name=FONT,
            font_size=int(self.scale * 15),
            anchor_x="center",
        )


class WordCloud:
    """
    Arrange words in an interactive word cloud

    """

    highlight_scale = 2.0

    def __init__(self, center_x: float, center_y: float, width: float, height: float, words: list = None):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self._words = list() if words is None else words
        self._arrange_words()
        self.highlighted_word = None

    def _arrange_words(self):
        for word in self._words:
            word.center_x = self.center_x + (random.random() - 0.5) * self.width
            word.center_y = self.center_y + (random.random() - 0.5) * self.height

    def append(self, word: Word):
        self._words.append(word)
        self._arrange_words()

    def on_mouse_motion(self, x, y):
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

    def draw(self):
        for word in self._words:
            word.draw()
