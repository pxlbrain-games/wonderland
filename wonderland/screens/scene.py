from wonderland.screens.screen_base import Screen
from wonderland.ui import CardRow, Card, CardType, WordCloud, Word


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
            self.player_hand.append(Card(CardType.CHARACTER, "Foobar", "Bizbaz"))
        self.ui_elements.append(self.player_hand)
        self.ui_elements.append(self.word_cloud)

    def update(self, time_delta: float) -> None:
        pass
