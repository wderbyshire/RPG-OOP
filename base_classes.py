from typing import TypedDict, Literal


class BuffAbstractClass:
    def __init__(self):
        self.bonus_health: int | float = 0
        self.bonus_attack: int | float = 0
        self.bonus_defence: int | float = 0
        self.bonus_accuracy: int | float = 0

        self.bonus_initiative: int | float = 0
        self.bonus_crit: int | float = 0
        self.bonus_crit_mult: int | float = 0


class AffectedAttribute(BuffAbstractClass):
    def __init__(self):
        super().__init__()
        self.target: Literal["self", "enemy", "all", "everyone"] = "self"
        self.turn_count: int | None = None
        self.turns_affected: int | None = None
        self.turn_type: Literal["continuous", "flat"] = "flat"


class AbilityItem:
    def __init__(self):
        self.ability_name: str = ""
        self.ability_use_text: str = ""
        self.turn_description: str = ""
        self.stop_description: str = ""

        self.attributes_affected: list[AffectedAttribute] = []


class Armor(BuffAbstractClass):
    def __init__(self):
        super().__init__()
        self.name: str = ""
        self.slot: Literal["head", "chest", "arms", "ring", "legs", "feet"] = ""


class Weapon(BuffAbstractClass):
    def __init__(self):
        super().__init__()
        self.name: str = ""
        self.type: Literal["sword", "shield"] = ""
        self.dual_wield: bool = False
        self.weapon_abilities: list[AbilityItem] = []


class ArmorDict(TypedDict):
    head: Armor | None
    chest: Armor | None
    arms: Armor | None
    rings: tuple[Armor | None, Armor | None, Armor | None]
    legs: Armor | None
    feet: Armor | None


class WeaponDict(TypedDict):
    left: Weapon | None
    right: Weapon | None


class BaseCharacter:
    def __init__(self):
        self.entity_type: Literal["player", "enemy"] = 'enemy'
        self.name: str = ''
        self.archetype: str = ""
        self.current_health: int = 0
        self.max_health: int = 0

        self.base_attack: int = 0
        self.base_defence: int = 0
        self.base_health: int = 0
        self.base_accuracy: float = 0.0
        self.base_initiative: int = 0
        self.attack_disparity: int = 0
        self.base_crit: float = 0.0
        self.base_crit_multiplier: float = 0.0

        self.armor_slots: ArmorDict = {
            "head": None,
            "chest": None,
            "arms": None,
            "rings": (None, None, None),
            "legs": None,
            "feet": None
        }

        self.weapon_slots: WeaponDict = {
            "left": None,
            "right": None
        }

        self.inventory: list[AbilityItem] = []

        self.base_abilities: list[AbilityItem] = []

        self.gold: int = 0
        self.turn_position: int = 0
        self.exp: int = 0
        self.temp_stats_list: list[AffectedAttribute] = []

        self.Level: int = 0
