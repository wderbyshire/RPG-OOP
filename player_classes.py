from typing import TypedDict, Literal


class AttributeAffectDict(TypedDict):
    attribute: Literal["health", "defence", "attack", "accuracy", "crit", "crit_mult", "initiative", "reach"]
    target: Literal["self", "enemy", "all", "everyone"]
    amount: int | float
    turn_count: int | None
    turns_affected: int | None
    turn_type: Literal["continuous", "flat"]

class Ability:
    def __init__(self):
        self.ability_name: str = ""
        self.ability_use_text: str = ""
        self.turn_description: str = ""
        self.stop_description: str = ""

        self.attributes_affected: list[AttributeAffectDict] = []



#: ability id
# ability name# ability description
# ability use text
# target type [enemy, self]
# attributes affected
# values
# turn counter
# turn description
# stop description
# turn effect [flat, cont]
# damage bool
# added damage

class Armor:
    def __init__(self):
        self.bonus_health = 0
        self.bonus_attack = 0
        self.bonus_defence = 0
        self.bonus_accuracy = 0

        self.bonus_initiative = 0
        self.bonus_crit = 0
        self.bonus_crit_mult = 0
        self.bonus_reach = 0

class Weapon:
    def __init__(self):
        self.bonus_health = 0
        self.bonus_attack = 0
        self.bonus_defence = 0
        self.bonus_accuracy = 0

        self.bonus_initiative = 0
        self.bonus_crit = 0
        self.bonus_crit_mult = 0
        self.bonus_reach = 0

        self.weapon_abilities: list[Ability] = []


class ArmorDict(TypedDict):
    head: Armor | None
    chest: Armor | None
    arms: Armor | None
    rings: tuple[Armor | None, Armor | None, Armor | None]
    legs: Armor | None
    feet: Armor | None


class WeaponDict(TypedDict):
    primary: Weapon | None
    secondary: Weapon | None


class BaseCharacter:
    def __init__(self):
        self.entity_type = 'enemy'
        self.name = ''
        self.current_health = 0
        self.max_health = 0

        self.base_attack = 0
        self.base_defence = 0
        self.base_health = 0
        self.base_accuracy = 0

        self.armor_ids: ArmorDict = {
            "head": None,
            "chest": None,
            "arms": None,
            "rings": (None, None, None),
            "legs": None,
            "feet": None
        }

        self.weapon_ids: WeaponIdDict = {
            "primary": None,
            "secondary": None
        }

        self.gold = 0
        self.initiative = 0
        self.reach = 0
        self.turn_counter = 0
        self.attack_disparity = (0, 0)
        self.crit = 0
        self.crit_multiplier = 0
        self.exp = 0

        self.items = []
        self.abilities = []
        self.temp_stats_list = {}

        self.Level = 0



"",  # 0: Name of player
    "player",  # 1: Entity type
    0,  # 2: base attack
    0,  # 3: base defence
    0,  # 4: base health
    [],  # 5: Armor ids
    0.0,  # 6: Crit chance
    1.5,  # 7: Crit multiplier
    [],  # 8: Equipped weapon ids
    [],  # 9: Collected items ids
    0,  # 10: Gold
    0.0,  # 11: Accuracy %age
    0,  # 12: Initiative
    [],  # 13: Ability IDs
    0,  # 14: Archetype ID
    [],  # 15: Status effects
    0,  # 16: Current Health
    0,  # 17: Max Health