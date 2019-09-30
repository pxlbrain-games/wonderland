from abc import ABC, abstractmethod, abstractproperty

import arcade

class UIElement(ABC):
    """
    Abstract base class for Wonderland UI elements.

    """

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


class Rectangle:
    """
    Mixin that implements center_x, center_y, width and height properties.

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


class ClickableRectangle(Clickable, Rectangle):
    """
    Mixin that implements a collides_with_point method.

    """

    def collides_with_point(self, point: arcade.arcade_types.Point) -> bool:
        return (self.center_x - self.width / 2 < point[0] < self.center_x + self.width / 2) and (
            self.center_y - self.height / 2 < point[1] < self.center_y + self.height / 2
        )
