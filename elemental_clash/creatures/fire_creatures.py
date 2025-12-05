# creatures/fire_creatures.py
from __future__ import annotations
from typing import List
from creatures.base_creature import Creature
from abilities import Ability


class FireCreature(Creature):
    """
    Base class for all Fire element creatures.
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
        super().__init__(name, "Fire", max_hp, attack, defense, speed, abilities)

    def get_elemental_bonus(self, enemy_element: str) -> float:
        # Fire - Strong vs Air, Earth; Weak vs Water
        if enemy_element in ("Air", "Earth"):
            return 1.5
        if enemy_element == "Water":
            return 0.5
        return 1.0


# ------------ Abilities ------------ #

FLAME_DASH = Ability(
    "Flame Dash",
    "A fast fiery charge at the enemy.",
    ep_cost=15,
    effect_type="damage",
    power=18,
)

BURNING_AURA = Ability(
    "Burning Aura",
    "Surrounds the enemy in searing flames.",
    ep_cost=20,
    effect_type="damage",
    power=22,
)

METEOR_STRIKE = Ability(
    "Meteor Strike",
    "Calls down a blazing meteor for massive damage.",
    ep_cost=25,
    effect_type="damage",
    power=28,
)

VOLCANIC_RAGE = Ability(
    "Volcanic Rage",
    "Unleashes erupting flames, increasing attack temporarily.",
    ep_cost=20,
    effect_type="buff",
    power=10,  # buff strength (Dev B can interpret)
)

FIRE_FANG = Ability(
    "Fire Fang",
    "A vicious fiery bite.",
    ep_cost=15,
    effect_type="damage",
    power=20,
)

PACK_HOWL = Ability(
    "Pack Howl",
    "A rallying howl that boosts allied attack.",
    ep_cost=15,
    effect_type="buff",
    power=8,
)

# ------------ Concrete Fire Creatures ------------ #


class Emberfox(FireCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Emberfox",
            max_hp=28,
            attack=14,
            defense=4,
            speed=13,
            abilities=[FLAME_DASH, BURNING_AURA],
        )


class Infernosaur(FireCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Infernosaur",
            max_hp=45,
            attack=18,
            defense=3,
            speed=6,
            abilities=[METEOR_STRIKE, VOLCANIC_RAGE],
        )


class Blazewolf(FireCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Blazewolf",
            max_hp=32,
            attack=15,
            defense=5,
            speed=11,
            abilities=[FIRE_FANG, PACK_HOWL],
        )
