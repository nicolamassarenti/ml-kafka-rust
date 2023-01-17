import os

from confluent_kafka import Producer as KafkaProducer
import socket

from data_generator import logger


class Producer:
    @staticmethod
    def acked(err, msg):
        if err is not None:
            logger.error("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            logger.debug("Message produced: %s" % (str(msg)))

    @staticmethod
    def produce(image: bytes, endpoint: str, topic: str) -> None:
        """
        Sends the image to the endpoint using Kafka, publishing it to the topic
        :param image: the image to send as bytes
        :param endpoint: the endpoint to send the image to
        :param topic: the topic to publish the image to
        :return: None
        """
        logger.debug("Sending data with Kafka")
        # Creating the producer object
        conf = {"bootstrap.servers": endpoint, "client.id": socket.gethostname()}
        logger.debug("Creating the Kafka producer - conf: {conf}".format(conf=conf))
        producer = KafkaProducer(conf)

        # Sending data asynchronously
        producer.produce(topic, key="image", value="something", callback=Producer.acked)

        # Wait up to 1 second for events. Callbacks will be invoked during
        # this method call if the message is acknowledged.
        producer.poll(0.1)
