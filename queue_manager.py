import json
import sys
import time
import os

from common.rabbitmq import RabbitMqClient
from services.event_service import EventService


def main():
    client = RabbitMqClient
    try:
        while 1:
            start = time.time()
            events = EventService.get_all_events()

            if len(events) > 0:
                for event in events:
                    client.channel.basic_publish(exchange='', routing_key=os.environ['RABBITMQ_QUEUE'],
                                                 body=f"{json.dumps(event.__dict__)}")
                    EventService.mark_event_as_in_queue(event.eventID)

                print(f"Inserted {len(events)} events into queue")
            else:
                print(f"Inserted 0 events into queue")

            print(f"Duration: {time.time() - start}")
            time.sleep(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        client.connection.close()


if __name__ == "__main__":
    main()
