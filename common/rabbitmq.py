import os
import pika
from dotenv import load_dotenv

load_dotenv()

class RabbitMqClient:

    connection = None
    channel = None

    def __init__(self):

        parameters = pika.ConnectionParameters(host=os.environ['RABBITMQ_HOST'], port=os.environ['RABBITMQ_PORT'])

        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=os.environ['RABBITMQ_QUEUE'], durable=True)


