import os

from kafka import KafkaProducer

from data_generator import logger

class Sender:
    @staticmethod
    def send(image: bytes, endpoint: str) -> None:
        """
        Sends the `image` to the `endpoint` through Kafka
        """
        # Retrieve topic from env variable
        topic = os.getenv("TOPIC")

        logger.debug("Sending data with Kafka")
        # Creating the producer object
        producer = KafkaProducer(bootstrap_servers=endpoint)
        # Sending data asynchronously
        producer.send(topic=topic, value=image)
        # Block until all pending messages are at least put on the network
        producer.flush()
