import os
from common.mysql import MysqlClient
from dotenv import load_dotenv

from entities.event import Event

load_dotenv()


class EventService:

    @staticmethod
    def mark_event_as_in_queue(eventID: int):
        mysql_client = MysqlClient()
        cursor = mysql_client.connection.cursor()
        cursor.execute(f"UPDATE {os.environ['DB_NAME']}.events SET inQueue = 1 WHERE eventID = {eventID};")
        mysql_client.connection.commit()

    @staticmethod
    def get_all_events():

        mysql_client = MysqlClient()

        cursor = mysql_client.connection.cursor()

        cursor.execute(
            f"SELECT * FROM {os.environ['DB_NAME']}.events WHERE endTime < UNIX_TIMESTAMP() AND processed = 0 AND inQueue = 0;")
        result = cursor.fetchall()

        if result is None or len(result) == 0:
            return []

        event_list = []

        for row in result:
            event_list.append(Event(row))

        return event_list
