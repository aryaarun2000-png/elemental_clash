# creatures/air_creatures.py
from __future__ import annotations
from typing import List
from creatures.base_creature import Creature
from abilities import Ability


class AirCreature(Creature):
    """
    Base class for all Air element creatures.
    """

    def __init__(
        self,
        name: str,
        max_hp: int,
        attack: int,
        defense: int,
        speed: int,
        abilities: List[Ability],
    ) -> None:
        super().__init__(name, "Air", max_hp, attack, defense, speed, abilities)

    def get_elemental_bonus(self, enemy_element: str) -> float:
        # Air - Strong vs Water, Lightning; Weak vs Fire, Earth
        if enemy_element in ("Water", "Lightning"):
            return 1.5
        if enemy_element in ("Fire", "Earth"):
            return 0.5
        return 1.0


# ------------ Abilities ------------ #

WIND_SLASH = Ability(
    "Wind Slash",
    "A razor-sharp blade of wind cuts the foe.",
    ep_cost=15,
    effect_type="damage",
    power=18,
)

EVASION = Ability(
    "Evasion",
    "Uses swift movements to increase dodge chance.",
    ep_cost=15,
    effect_type="buff",
    power=10,
)

GUST_CANNON = Ability(
    "Gust Cannon",
    "Fires a concentrated blast of air.",
    ep_cost=18,
    effect_type="damage",
    power=21,
)

TAILWIND = Ability(
    "Tailwind",
    "A supporting wind that boosts speed.",
    ep_cost=15,
    effect_type="buff",
    power=10,
)

HURRICANE = Ability(
    "Hurricane",
    "A violent storm batters the enemy.",
    ep_cost=25,
    effect_type="damage",
    power=26,
)

NIGHT_VISION = Ability(
    "Night Vision",
    "Sharpens senses, improving accuracy and evasion.",
    ep_cost=15,
    effect_type="buff",
    power=9,
)

# ------------ Concrete Air Creatures ------------ #


class Zephyrwing(AirCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Zephyrwing",
            max_hp=25,
            attack=11,
            defense=4,
            speed=15,
            abilities=[WIND_SLASH, EVASION],
        )


class Cloudstrider(AirCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Cloudstrider",
            max_hp=30,
            attack=12,
            defense=5,
            speed=14,
            abilities=[GUST_CANNON, TAILWIND],
        )


class Tempestowl(AirCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Tempestowl",
            max_hp=33,
            attack=13,
            defense=6,
            speed=12,
            abilities=[HURRICANE, NIGHT_VISION],
        )
