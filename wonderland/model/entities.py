from typing import List


class CharacterArchetype:
    def __init__(self, name: str, unique: bool):
        self.name: str = name
        self.unique: bool = unique


class Character:

    archetypes: List[CharacterArchetype] = [
        CharacterArchetype("The Monarch", True),
        CharacterArchetype("The Mad One", True),
        CharacterArchetype("A Critter", False),
    ]

    def __init__(self, name: str, archetype: CharacterArchetype):
        self.name: str = name
        self.archetype: CharacterArchetype = archetype


class Place:
    pass


class Thing:
    pass
