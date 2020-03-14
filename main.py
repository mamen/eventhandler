from common.mysql import MysqlClient
from entities.event import Event
from entities.mission_type import MissionType
from services.planet_service import PlanetService


def processAttack(event: Event):
    print("ATTACK:")
    print(f"{event.startID} vs. {event.endID}")


def processTransport(event: Event):

    if event.returning:
        start_planet = PlanetService().get_planet_by_id(event.startID)

        print(start_planet.name)
    else:
        start_planet = PlanetService().get_planet_by_id(event.startID)

        print(start_planet.name)
        print("TRANSPORT:")


def main():

    mysql = MysqlClient()

    event: Event = mysql.get_event(event_id)

    mission_type = MissionType(event.mission)

    if mission_type == MissionType.TRANSPORT:
        print("Processing TRANSPORT")
        processTransport(event)
    elif mission_type == MissionType.DEPLOY:
        print("Processing DEPLOY")
    elif mission_type == MissionType.ATTACK:
        print("Processing ATTACK")
        processAttack(event)
    elif mission_type == MissionType.ACS:
        print("Processing ACS")
    elif mission_type == MissionType.HOLD:
        print("Processing HOLD")
    elif mission_type == MissionType.COLONIZE:
        print("Processing COLONIZE")
    elif mission_type == MissionType.HARVEST:
        print("Processing HARVEST")
    elif mission_type == MissionType.ESPIONAGE:
        print("Processing ESPIONAGE")
    elif mission_type == MissionType.DESTROY:
        print("Processing DESTROY")
    else:
        print(f"ERROR: MissionType {event.mission} invalid")


if __name__ == "__main__":
    main()
