# creatures/water_creatures.py
from __future__ import annotations
from typing import List
from creatures.base_creature import Creature
from abilities import Ability


class WaterCreature(Creature):
    """
    Base class for all Water element creatures.
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
        super().__init__(name, "Water", max_hp, attack, defense, speed, abilities)

    def get_elemental_bonus(self, enemy_element: str) -> float:
        # Water - Strong vs Fire, Earth; Weak vs Lightning
        if enemy_element in ("Fire", "Earth"):
            return 1.5
        if enemy_element == "Lightning":
            return 0.5
        return 1.0


# ------------ Abilities ------------ #

TIDAL_WAVE = Ability(
    "Tidal Wave",
    "A massive wave crashes into the opponent.",
    ep_cost=22,
    effect_type="damage",
    power=24,
)

SHELL_SHIELD = Ability(
    "Shell Shield",
    "Forms a tough shell that increases defense.",
    ep_cost=15,
    effect_type="buff",
    power=10,
)

AQUA_JET = Ability(
    "Aqua Jet",
    "A quick high-speed water strike.",
    ep_cost=15,
    effect_type="damage",
    power=18,
)

HEALING_RAIN = Ability(
    "Healing Rain",
    "Soothing rain restores health over the battlefield.",
    ep_cost=20,
    effect_type="heal",
    power=20,
)

ICE_SHARD = Ability(
    "Ice Shard",
    "Launches a sharp shard of ice.",
    ep_cost=15,
    effect_type="damage",
    power=17,
)

FROZEN_TOUCH = Ability(
    "Frozen Touch",
    "A chilling touch that slows and weakens the foe.",
    ep_cost=20,
    effect_type="debuff",
    power=12,
)

# ------------ Concrete Water Creatures ------------ #


class Aquashell(WaterCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Aquashell",
            max_hp=40,
            attack=10,
            defense=9,
            speed=7,
            abilities=[TIDAL_WAVE, SHELL_SHIELD],
        )


class Tidalfin(WaterCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Tidalfin",
            max_hp=30,
            attack=13,
            defense=6,
            speed=12,
            abilities=[AQUA_JET, HEALING_RAIN],
        )


class Frostbite(WaterCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Frostbite",
            max_hp=35,
            attack=12,
            defense=7,
            speed=9,
            abilities=[ICE_SHARD, FROZEN_TOUCH],
        )
