# abilities/ability.py
from __future__ import annotations
from typing import Literal, Dict, Any

# Allowed effect types from the PDF
EffectType = Literal["damage", "heal", "buff", "debuff", "special"]


class Ability:
    """
    Represents a creature ability (e.g. Flame Dash, Healing Rain).
    Matches the Ability specification in the project PDF.
    """

    def __init__(
        self,
        name: str,
        description: str,
        ep_cost: int,
        effect_type: EffectType,
        power: int,
    ) -> None:
        if not (10 <= ep_cost <= 30):
            raise ValueError("EP cost must be between 10 and 30.")

        self.name = name
        self.description = description
        self.ep_cost = ep_cost
        self.effect_type = effect_type
        self.power = power

    def execute(self, user, target) -> Dict[str, Any]:
        """
        Execute the ability effect.

        For now, this method does not directly change HP/EP.
        It returns a dictionary describing the effect that
        BattleCalculator and Player can interpret.
        """
        return {
            "ability_name": self.name,
            "effect_type": self.effect_type,
            "power": self.power,
            "ep_cost": self.ep_cost,
            "user": user,
            "target": target,
        }

    def __str__(self) -> str:
        return f"{self.name} ({self.effect_type}, EP: {self.ep_cost})"
