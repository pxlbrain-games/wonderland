from enum import Enum
from typing import Dict, Callable

import arcade

from wonderland.ui.config import FONT
from wonderland.ui.ui_element_base import UIElement, Clickable, Rectangle


class ButtonState(Enum):
    NORMAL = 1
    HOVER = 2
    PRESSED = 3


class Button(UIElement, Rectangle, Clickable):
    """
    A clickable button with text.

    """

    font: str = FONT
    font_size: int = 16
    color: Dict[ButtonState, Dict[str, arcade.arcade_types.Color]] = {
        ButtonState.NORMAL: {
            "text": arcade.color.BLACK,
            "background": arcade.color.BEIGE,
            "outline": arcade.color.DARK_VANILLA,
        },
        ButtonState.HOVER: {
            "text": arcade.color.BLACK,
            "background": arcade.color.BEIGE,
            "outline": arcade.color.DARK_VANILLA,
        },
        ButtonState.PRESSED: {
            "text": arcade.color.BLACK,
            "background": arcade.color.DARK_VANILLA,
            "outline": arcade.color.BEIGE,
        },
    }

    def __init__(
        self,
        text: str,
        center_x: float,
        center_y: float,
        width: float = None,
        height: float = None,
        scale: float = 1.0,
        on_click: Callable = None,
    ) -> None:
        self.text: str = text
        self.center_x = center_x
        self.center_y = center_y
        self.width = width if width is not None else len(text) * scale * self.font_size * 0.6
        self.height = height if height is not None else scale * self.font_size * 1.25
        self.scale: float = scale
        self._on_click: Callable = on_click if on_click is not None else lambda: None
        self.state: ButtonState = ButtonState.NORMAL
        self.background: Dict[ButtonState, arcade.ShapeElementList] = {
            ButtonState.NORMAL: arcade.ShapeElementList(),
            ButtonState.HOVER: arcade.ShapeElementList(),
            ButtonState.PRESSED: arcade.ShapeElementList(),
        }
        for state in ButtonState:
            self.background[state].append(
                arcade.create_rectangle_filled(
                    center_x=center_x,
                    center_y=center_y,
                    width=self.width,
                    height=self.height,
                    color=self.color[state]["background"],
                )
            )
            self.background[state].append(
                arcade.create_rectangle_outline(
                    center_x=center_x,
                    center_y=center_y,
                    width=self.width,
                    height=self.height,
                    color=self.color[state]["outline"],
                    border_width=2.0 * self.scale,
                )
            )

    def draw(self) -> None:
        self.background[self.state].draw()
        arcade.draw_text(
            text=self.text,
            start_x=self.center_x,
            start_y=self.center_y,
            color=self.color[self.state]["text"],
            font_size=int(self.scale * self.font_size),
            font_name=self.font,
            anchor_y="center",
            anchor_x="center",
        )

    def on_click(self) -> None:
        self.state = ButtonState.PRESSED
        self._on_click()
