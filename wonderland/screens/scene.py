from wonderland.screens.screen_base import Screen
from wonderland.ui import CardRow, Card, WordCloud, Word


class Scene(Screen):
    """
    Play a scene against Alice with a given deck of cards.

    """

    def __init__(self):
        # Initialize Sprites and SpriteLists and set them to None
        self.player_hand: CardRow = None
        self.word_cloud: WordCloud = None

    def setup(self, width: int, height: int) -> None:
        """Create and arrange the scenes Sprites."""
        self.word_cloud = WordCloud(width / 2, height * 0.8, width * 0.6, height * 0.2)
        for _ in range(5):
            self.word_cloud.append(Word("Hello"))
        self.player_hand = CardRow(width / 2, height * 0.2, min(width * 0.7, 724))
        for _ in range(8):
            self.player_hand.append(Card("Foobar"))

    def draw(self) -> None:
        self.word_cloud.draw()
        self.player_hand.draw()

    def update(self) -> None:
        pass

    def on_mouse_press(self, x: float, y: float, button) -> None:
        pass

    def on_mouse_motion(self, x: float, y: float) -> None:
        self.player_hand.on_mouse_motion(x, y)
        self.word_cloud.on_mouse_motion(x, y)
