import os
from common.mysql import MysqlClient
from dotenv import load_dotenv

from entities.planet import Planet

load_dotenv()


class PlanetService:

    def get_planet_by_id(self, planet_id):

        mysql_client = MysqlClient()

        cursor = mysql_client.connection.cursor()

        cursor.execute(f"SELECT * FROM {os.environ['DB_NAME']}.planets WHERE planetID = {planet_id}")

        result = cursor.fetchone()

        if len(result) == 0:
            return

        return Planet(result)