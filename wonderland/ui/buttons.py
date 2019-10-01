from enum import Enum
from typing import Dict, List, Callable, Optional, Any

import arcade

from wonderland.ui.config import FONT
from wonderland.ui.ui_element_base import UIElement, UIContainer, Clickable, Hoverable, Rectangle


class ButtonState(Enum):
    NORMAL = 1
    HOVER = 2
    PRESSED = 3
    INACTIVE = 4


class Button(UIElement, Rectangle, Clickable, Hoverable):
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
            "text": arcade.color.BALL_BLUE,
            "background": arcade.color.BEIGE,
            "outline": arcade.color.DARK_VANILLA,
        },
        ButtonState.PRESSED: {
            "text": arcade.color.BLACK,
            "background": arcade.color.DARK_VANILLA,
            "outline": arcade.color.BEIGE,
        },
        ButtonState.INACTIVE: {
            "text": arcade.color.GRAY,
            "background": arcade.color.DARK_GRAY,
            "outline": arcade.color.GRAY,
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
        on_click: Callable[[], None] = None,
    ) -> None:
        self.text: str = text
        self.center_x = center_x
        self.center_y = center_y
        self.width = width if width is not None else len(text) * scale * self.font_size * 0.6
        self.height = height if height is not None else scale * self.font_size * 1.4
        self.scale: float = scale
        self._on_click: Callable[[], None] = on_click if on_click is not None else lambda: None
        self.state: ButtonState = ButtonState.NORMAL
        self.background: Dict[ButtonState, arcade.ShapeElementList] = {
            state: arcade.ShapeElementList() for state in ButtonState
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

    def set_on_click(self, on_click: Callable[[], None]):
        self._on_click = on_click

    def on_click(self) -> None:
        if not (self.state == ButtonState.INACTIVE or self.state == ButtonState.PRESSED):
            self.state = ButtonState.PRESSED
            self._on_click()
        elif self.state == ButtonState.PRESSED:
            self.state = ButtonState.NORMAL
            self._on_click()

    def deactivate(self):
        self.state = ButtonState.INACTIVE

    def activate(self):
        self.state = ButtonState.NORMAL

    def on_hover(self):
        if not (self.state == ButtonState.INACTIVE or self.state == ButtonState.PRESSED):
            self.state = ButtonState.HOVER

    def on_hover_end(self):
        if self.state == ButtonState.HOVER:
            self.state = ButtonState.NORMAL


class ButtonChooser(UIContainer):
    def __init__(
        self,
        options: Dict[str, Any],
        center_x: float,
        center_y: float,
        width: float,
        on_choice: Callable[[Any], None] = None,
        on_choice_reset: Callable[[], None] = None,
    ):
        self._on_choice: Callable[[Any], None] = on_choice if on_choice is not None else lambda option: None
        self._on_choice_reset: Callable[[], None] = on_choice_reset if on_choice_reset is not None else lambda: None
        self._choice_taken: bool = False
        self._choice: Any = None
        self.buttons: List[Button] = list()
        for i, (text, option) in enumerate(options.items()):
            button = Button(
                text=text,
                center_x=(center_x + width * (i / (len(options) - 1) - 0.5) if len(options) > 1 else center_x),
                center_y=center_y,
                width=width / len(options) - 10.0,
                scale=1.3,
            )
            self._assign_on_click(button, option)
            self.buttons.append(button)
            self.ui_elements.append(button)

    @property
    def choice_taken(self) -> bool:
        return self._choice_taken

    @property
    def choice(self) -> Any:
        return self._choice

    def set_on_choice(self, on_choice: Callable[[Any], None]) -> None:
        self._on_choice = on_choice

    def set_on_choice_reset(self, on_choice_reset: Callable[[], None]) -> None:
        self._on_choice_reset = on_choice_reset

    def _assign_on_click(self, button: Button, option: Any) -> None:
        button.set_on_click(lambda: self._on_button_pressed(button, option))

    def _on_button_pressed(self, button_pressed: Button, option: Any) -> None:
        if not self.choice_taken:
            for button in self.buttons:
                if button is not button_pressed:
                    button.deactivate()
            self._choice = option
            self._on_choice(option)
            self._choice_taken = True
        else:
            for button in self.buttons:
                button.activate()
            self._choice = None
            self._on_choice_reset()
            self._choice_taken = False
