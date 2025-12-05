# creatures/earth_creatures.py
from __future__ import annotations
from typing import List
from creatures.base_creature import Creature
from abilities import Ability


class EarthCreature(Creature):
    """
    Base class for all Earth element creatures.
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
        super().__init__(name, "Earth", max_hp, attack, defense, speed, abilities)

    def get_elemental_bonus(self, enemy_element: str) -> float:
        # Earth - Strong vs Lightning, Air; Weak vs Fire, Water
        if enemy_element in ("Lightning", "Air"):
            return 1.5
        if enemy_element in ("Fire", "Water"):
            return 0.5
        return 1.0


# ------------ Abilities ------------ #

ROCK_THROW = Ability(
    "Rock Throw",
    "Hurls a large rock at the opponent.",
    ep_cost=15,
    effect_type="damage",
    power=16,
)

FORTIFY = Ability(
    "Fortify",
    "Hardens the body, greatly increasing defense.",
    ep_cost=20,
    effect_type="buff",
    power=15,
)

EARTHQUAKE = Ability(
    "Earthquake",
    "A powerful tremor that damages all enemies.",
    ep_cost=25,
    effect_type="damage",
    power=26,
)

BURROW = Ability(
    "Burrow",
    "Digs underground to avoid damage and prepare a strike.",
    ep_cost=15,
    effect_type="special",
    power=0,
)

IRON_SLAM = Ability(
    "Iron Slam",
    "A brutal slam with an iron-coated body.",
    ep_cost=18,
    effect_type="damage",
    power=20,
)

METAL_COAT = Ability(
    "Metal Coat",
    "Covers the body in metal, boosting attack and defense.",
    ep_cost=20,
    effect_type="buff",
    power=12,
)

# ------------ Concrete Earth Creatures ------------ #


class Stoneguard(EarthCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Stoneguard",
            max_hp=50,
            attack=8,
            defense=10,
            speed=5,
            abilities=[ROCK_THROW, FORTIFY],
        )


class Terraclaw(EarthCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Terraclaw",
            max_hp=38,
            attack=14,
            defense=8,
            speed=8,
            abilities=[EARTHQUAKE, BURROW],
        )


class Ironback(EarthCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Ironback",
            max_hp=42,
            attack=11,
            defense=9,
            speed=6,
            abilities=[IRON_SLAM, METAL_COAT],
        )
