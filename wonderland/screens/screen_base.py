from abc import ABC, abstractmethod


class Screen(ABC):
    """
    Abstract base class for Wonderland screens.

    """

    @abstractmethod
    def setup(self, width: int, height: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def on_mouse_motion(self, x: float, y: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def on_mouse_press(self, x: float, y: float) -> None:
        raise NotImplementedError
