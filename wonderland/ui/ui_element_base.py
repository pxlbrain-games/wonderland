from typing import List
from abc import ABC, abstractmethod

import arcade


class UIElement(ABC):
    """
    Abstract base class for Wonderland UI elements.

    """

    @property
    def z_value(self) -> float:
        if not hasattr(self, "_z_value"):
            self._z_value = 0.0
        return self._z_value

    @z_value.setter
    def z_value(self, value: float) -> None:
        self._z_value = value

    @abstractmethod
    def draw(self) -> None:
        raise NotImplementedError


class Clickable(ABC):
    """
    Abstract base class for stuff that can be clicked on.

    """

    @abstractmethod
    def collides_with_point(self, point: arcade.arcade_types.Point) -> bool:
        raise NotImplementedError

    @abstractmethod
    def on_click(self) -> None:
        raise NotImplementedError


class Hoverable(ABC):
    """
    Abstract base class for stuff that the mouse can hover over.

    """

    @property
    def hover_is_active(self) -> bool:
        if not hasattr(self, "_hover_is_active"):
            self._hover_is_active = False
        return self._hover_is_active

    @abstractmethod
    def collides_with_point(self, point: arcade.arcade_types.Point) -> bool:
        raise NotImplementedError

    @abstractmethod
    def on_hover(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def on_hover_end(self) -> None:
        raise NotImplementedError


class UIContainer(UIElement, ABC):

    active_hoverable: Hoverable = None

    @classmethod
    def _set_active_hoverable(cls, value: Hoverable):
        cls.active_hoverable = value

    @property
    def ui_elements(self) -> List[UIElement]:
        if not hasattr(self, "_ui_elements"):
            self._ui_elements: List[UIElement] = list()
        return self._ui_elements

    def draw(self) -> None:
        for ui_element in sorted(self.ui_elements, key=lambda el: el.z_value):
            ui_element.draw()

    def on_mouse_motion(self, x: float, y: float) -> None:
        for ui_element in self.ui_elements:
            if isinstance(ui_element, Hoverable) and ui_element.collides_with_point((x, y)):
                if ui_element is not self.active_hoverable:
                    if self.active_hoverable is not None:
                        self.active_hoverable.on_hover_end()
                        self.active_hoverable._hover_is_active = False
                    self._set_active_hoverable(ui_element)
                ui_element._hover_is_active = True
                ui_element.on_hover()
            elif isinstance(ui_element, Hoverable) and ui_element.hover_is_active:
                ui_element._hover_is_active = False
                ui_element.on_hover_end()
            if hasattr(ui_element, "_ui_elements") and hasattr(ui_element, "on_mouse_motion"):
                ui_element.on_mouse_motion(x, y)

    def on_mouse_press(self, x: float, y: float, button: int) -> None:
        for ui_element in self.ui_elements:
            if isinstance(ui_element, Clickable) and ui_element.collides_with_point((x, y)):
                if button is arcade.MOUSE_BUTTON_LEFT:
                    ui_element.on_click()
            if hasattr(ui_element, "_ui_elements") and hasattr(ui_element, "on_mouse_press"):
                ui_element.on_mouse_press(x, y, button)


class Rectangle:
    """
    Mixin that implements center_x, center_y, width and height properties and collides_with_point.

    """

    @property
    def center_x(self) -> float:
        return self._center_x if hasattr(self, "_center_x") else None

    @center_x.setter
    def center_x(self, value: float) -> None:
        self._center_x = value

    @property
    def center_y(self) -> float:
        return self._center_y if hasattr(self, "_center_y") else None

    @center_y.setter
    def center_y(self, value: float) -> None:
        self._center_y: float = value

    @property
    def width(self) -> float:
        return self._width if hasattr(self, "_width") else None

    @width.setter
    def width(self, value: float) -> None:
        self._width: float = value

    @property
    def height(self) -> float:
        return self._height if hasattr(self, "_height") else None

    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    def collides_with_point(self, point: arcade.arcade_types.Point) -> bool:
        return (self.center_x - self.width / 2 < point[0] < self.center_x + self.width / 2) and (
            self.center_y - self.height / 2 < point[1] < self.center_y + self.height / 2
        )
