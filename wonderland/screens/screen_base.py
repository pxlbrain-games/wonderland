from typing import List
from abc import ABC, abstractmethod

import arcade

from wonderland.ui import UIElement, UIContainer, Clickable, Hoverable


class Screen(UIContainer, ABC):
    """
    Abstract base class for Wonderland screens.

    """

    @abstractmethod
    def setup(self, width: int, height: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, delta_time: float) -> None:
        raise NotImplementedError
