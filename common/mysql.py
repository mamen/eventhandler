import os

import mysql.connector
from dotenv import load_dotenv
from entities.event import Event

load_dotenv()


class MysqlClient:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            passwd=os.environ['DB_PASS'],
            port=os.environ['DB_PORT'],
        )

    def get_event(self, event_id: int):
        cursor = self.connection.cursor()

        cursor.execute(f"SELECT * FROM {os.environ['DB_NAME']}.events WHERE eventID = {event_id}")

        result = cursor.fetchone()

        if len(result) == 0:
            return

        return Event(result)
