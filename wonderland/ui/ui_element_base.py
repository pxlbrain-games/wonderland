from abc import ABC, abstractmethod


class UIElement(ABC):
    """
    Abstract base class for Wonderland UI elements.

    """

    @abstractmethod
    def draw(self) -> None:
        raise NotImplementedError
