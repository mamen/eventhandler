from entities.missionType import MissionType
from entities.planetType import PlanetType


class Event:
    eventID: int
    ownerID: int
    mission: MissionType
    fleetlist: str  # dict[int, int]
    startID: int
    startType: PlanetType
    startTime: int
    endID: int
    endType: PlanetType
    endTime: int
    loadedMetal: float
    loadedCrystal: float
    loadedDeuterium: float
    returning: bool
    processed: bool

    def __init__(self, db_row):
        self.eventID, self.ownerID, self.mission, \
            self.fleetlist, self.startID, self.startType, \
            self.startTime, self.endID, self.endType, \
            self.endTime, self.loadedMetal, self.loadedCrystal, \
            self.loadedDeuterium, self.returning, self.processed = db_row
