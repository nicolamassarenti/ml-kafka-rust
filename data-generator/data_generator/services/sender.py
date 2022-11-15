import os

from kafka import KafkaProducer

from data_generator import logger


class Sender:
    @staticmethod
    def send(image: bytes, endpoint: str, topic: str) -> None:
        """
        Sends the image to the endpoint using Kafka, publishing it to the topic
        :param image: the image to send as bytes
        :param endpoint: the endpoint to send the image to
        :param topic: the topic to publish the image to
        :return: None
        """
        logger.debug("Sending data with Kafka")
        # Creating the producer object
        producer = KafkaProducer(bootstrap_servers=endpoint)

        # Sending data asynchronously
        producer.send(topic=topic, value=image)
        # Block until all pending messages are at least put on the network
        producer.flush()
