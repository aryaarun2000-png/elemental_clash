# creatures/base_creature.py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from abilities import Ability


class Creature(ABC):
    """
    Abstract base class for all creatures.

    Required attributes and methods are taken from section 5.1
    in the Elemental Clash project specification.
    """

    def __init__(
        self,
        name: str,
        element: str,
        max_hp: int,
        attack: int,
        defense: int,
        speed: int,
        abilities: List[Ability],
    ) -> None:
        self.name = name
        self.element = element
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

        if len(abilities) != 2:
            raise ValueError(f"{name} must have exactly 2 abilities.")
        self.abilities = abilities

    # ---------- Required methods ---------- #

    def is_alive(self) -> bool:
        """Return True if current_hp > 0."""
        return self.current_hp > 0

    def take_damage(self, amount: int) -> tuple[int, bool]:
        """
        Apply damage and return (actual_damage, was_defeated).
        Minimum damage is always 1.
        """
        actual = max(1, int(amount))
        self.current_hp -= actual

        if self.current_hp < 0:
            self.current_hp = 0

        return actual, not self.is_alive()

    def heal(self, amount: int) -> int:
        """
        Heal the creature and return the actual amount healed.
        """
        if amount <= 0:
            return 0
        before = self.current_hp
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        return self.current_hp - before

    @abstractmethod
    def get_elemental_bonus(self, enemy_element: str) -> float:
        """
        Return 1.5, 1.0, or 0.5 based on elemental matchup.
        Must be overridden in each element subclass.
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """
        Formatted string representation used by the Display system.
        """
        return (
            f"{self.name} ({self.element}) - "
            f"HP: {self.current_hp}/{self.max_hp} | "
            f"ATK: {self.attack} | DEF: {self.defense} | SPD: {self.speed}"
        )
