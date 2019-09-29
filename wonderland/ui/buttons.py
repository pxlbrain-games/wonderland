import arcade

from wonderland.ui.config import FONT
from wonderland.ui.ui_element_base import UIElement


class Button(UIElement):
    """
    A clickable button with text.

    """

    font: str = FONT
    font_size: int = 16
    text_color: arcade.arcade_types.Color = arcade.color.BLACK
    background_color: arcade.arcade_types.Color = arcade.color.BEIGE

    def __init__(
        self,
        text: str,
        center_x: float,
        center_y: float,
        width: float = None,
        height: float = None,
        scale: float = 1.0,
    ) -> None:
        self.text: str = text
        self._center_x: float = center_x
        self._center_y: float = center_y
        self.width: float = width if width is not None else len(text) * scale * self.font_size * 0.6
        self.height: float = height if height is not None else scale * self.font_size * 1.25
        self.scale = 1.0
        self.background = arcade.create_rectangle_filled(
            center_x=center_x, center_y=center_y, width=self.width, height=self.height, color=self.background_color
        )

    def draw(self) -> None:
        self.background.draw()
        arcade.draw_text(
            text=self.text,
            start_x=self._center_x,
            start_y=self._center_y,
            color=self.text_color,
            font_size=int(self.scale * self.font_size),
            font_name=self.font,
            anchor_y="center",
            anchor_x="center",
        )
