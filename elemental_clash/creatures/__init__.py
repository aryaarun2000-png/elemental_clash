# creatures/__init__.py
from .base_creature import Creature
from .fire_creatures import FireCreature, Emberfox, Infernosaur, Blazewolf
from .water_creatures import WaterCreature, Aquashell, Tidalfin, Frostbite
from .earth_creatures import EarthCreature, Stoneguard, Terraclaw, Ironback
from .air_creatures import AirCreature, Zephyrwing, Cloudstrider, Tempestowl
from .lightning_creatures import (
    LightningCreature,
    Sparkfang,
    Thundermane,
    Voltwing,
)

__all__ = [
    "Creature",
    "FireCreature",
    "WaterCreature",
    "EarthCreature",
    "AirCreature",
    "LightningCreature",
    "Emberfox",
    "Infernosaur",
    "Blazewolf",
    "Aquashell",
    "Tidalfin",
    "Frostbite",
    "Stoneguard",
    "Terraclaw",
    "Ironback",
    "Zephyrwing",
    "Cloudstrider",
    "Tempestowl",
    "Sparkfang",
    "Thundermane",
    "Voltwing",
]
