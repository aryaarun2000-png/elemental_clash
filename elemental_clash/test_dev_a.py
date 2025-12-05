# test_dev_a.py

from creatures.fire_creatures import Emberfox, Infernosaur, Blazewolf
from creatures.water_creatures import Aquashell, Tidalfin, Frostbite
from creatures.earth_creatures import Stoneguard, Terraclaw, Ironback
from creatures.air_creatures import Zephyrwing, Cloudstrider, Tempestowl
from creatures.lightning_creatures import Sparkfang, Thundermane, Voltwing

# Test creating one creature
emberfox = Emberfox()
print(emberfox)
print("Abilities:", [str(a) for a in emberfox.abilities])
print()

# Test elemental bonus
other_element = "Water"
print("Fire vs Water bonus:", emberfox.get_elemental_bonus(other_element))

# Test damage
damage, defeated = emberfox.take_damage(10)
print(f"Took {damage} damage. Defeated? {defeated}")
print("Current HP:", emberfox.current_hp)

# Test healing
healed = emberfox.heal(5)
print(f"Healed {healed}. HP now:", emberfox.current_hp)
