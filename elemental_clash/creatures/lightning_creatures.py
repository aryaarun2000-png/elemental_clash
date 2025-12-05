# creatures/lightning_creatures.py
from __future__ import annotations
from typing import List
from creatures.base_creature import Creature
from abilities import Ability


class LightningCreature(Creature):
    """
    Base class for all Lightning element creatures.
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
        super().__init__(name, "Lightning", max_hp, attack, defense, speed, abilities)

    def get_elemental_bonus(self, enemy_element: str) -> float:
        # Lightning - Strong vs Water, Air; Weak vs Earth
        if enemy_element in ("Water", "Air"):
            return 1.5
        if enemy_element == "Earth":
            return 0.5
        return 1.0


# ------------ Abilities ------------ #

THUNDER_FANG = Ability(
    "Thunder Fang",
    "A shocking bite that can jolt the enemy.",
    ep_cost=18,
    effect_type="damage",
    power=22,
)

STATIC_SHOCK = Ability(
    "Static Shock",
    "A jolt of static that weakens and slows the foe.",
    ep_cost=18,
    effect_type="debuff",
    power=12,
)

LIGHTNING_BOLT = Ability(
    "Lightning Bolt",
    "A focused bolt of lightning strikes the target.",
    ep_cost=22,
    effect_type="damage",
    power=26,
)

CHARGE_UP = Ability(
    "Charge Up",
    "Stores electricity to boost the next attack.",
    ep_cost=15,
    effect_type="buff",
    power=12,
)

STORM_STRIKE = Ability(
    "Storm Strike",
    "A rapid strike enhanced by storm energy.",
    ep_cost=20,
    effect_type="damage",
    power=23,
)

PARALYSIS = Ability(
    "Paralysis",
    "Overloads the opponent with electricity, hindering movement.",
    ep_cost=20,
    effect_type="debuff",
    power=15,
)

# ------------ Concrete Lightning Creatures ------------ #


class Sparkfang(LightningCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Sparkfang",
            max_hp=27,
            attack=16,
            defense=4,
            speed=14,
            abilities=[THUNDER_FANG, STATIC_SHOCK],
        )


class Thundermane(LightningCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Thundermane",
            max_hp=36,
            attack=17,
            defense=5,
            speed=11,
            abilities=[LIGHTNING_BOLT, CHARGE_UP],
        )


class Voltwing(LightningCreature):
    def __init__(self) -> None:
        super().__init__(
            name="Voltwing",
            max_hp=24,
            attack=15,
            defense=3,
            speed=15,
            abilities=[STORM_STRIKE, PARALYSIS],
        )
