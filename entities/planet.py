

class Planet:


    def __init__(self, db_row):
        self.planetID, self.ownerID, self.name, self.posGalaxy, self.posSystem, self.posPlanet, self.lastUpdate, self.planetType, self.image, self.diameter, self.fieldsCurrent, self.fieldsMax, self.tempMin, self.tempMax, self.metal, self.crystal, self.deuterium, self.energyUsed, self.energyMax, self.metalMinePercent, self.crystalMinePercent, self.deuteriumSynthesizerPercent, self.solarPlantPercent, self.fusionReactorPercent, self.solarSatellitePercent, self.bBuildingId, self.bBuildingEndTime, self.bBuildingDemolition, self.bHangarQueue, self.bHangarStartTime, self.bHangarPlus, self.destroyed = db_row