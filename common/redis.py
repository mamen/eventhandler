import math
import os
import time

import redis
from dotenv import load_dotenv

load_dotenv()


class RedisClient:

    def __init__(self):
        self.client = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=0,
                                        password=os.environ['REDIS_PASSWORD'], socket_timeout=None,
                                        connection_pool=None, charset='utf-8', errors='strict', unix_socket_path=None,
                                        decode_responses=True)

    def get_unprocessed_event(self):
        events = self.client.zrangebyscore("eventQueue", 0, math.floor(time.time()), withscores=True)

        if len(events) == 0:
            return

        event = self.client.zpopmin("eventQueue")

        event_id, _ = event[0]

        return event_id
