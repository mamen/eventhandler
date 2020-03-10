from common.mysql import MysqlClient
from common.redis import RedisClient
from entities.event import Event
from entities.missionType import MissionType


def main():
    redis = RedisClient()

    event_id = redis.get_unprocessed_event()

    if event_id is None:
        print("ERROR: event not found")
        return

    mysql = MysqlClient()

    event: Event = mysql.get_event(event_id)

    if event.mission == MissionType.TRANSPORT:
        print("Processing TRANSPORT")
    elif event.mission == MissionType.DEPLOY:
        print("Processing DEPLOY")
    elif event.mission == MissionType.ATTACK:
        print("Processing ATTACK")
    elif event.mission == MissionType.ACS:
        print("Processing ACS")
    elif event.mission == MissionType.HOLD:
        print("Processing HOLD")
    elif event.mission == MissionType.COLONIZE:
        print("Processing COLONIZE")
    elif event.mission == MissionType.HARVEST:
        print("Processing HARVEST")
    elif event.mission == MissionType.ESPIONAGE:
        print("Processing ESPIONAGE")
    elif event.mission == MissionType.DESTROY:
        print("Processing DESTROY")
    else:
        print(f"ERROR: MissionType {event.mission} invalid")

    print(event.endTime)


if __name__ == "__main__":
    main()
