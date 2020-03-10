from enum import Enum


class MissionType(Enum):
    TRANSPORT = 0
    DEPLOY = 1
    ATTACK = 2
    ACS = 3
    HOLD = 4
    COLONIZE = 5
    HARVEST = 6
    ESPIONAGE = 7
    DESTROY = 8
