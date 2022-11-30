from typing import Dict, Any

from pydantic import BaseModel, Field
from confluent_kafka import Consumer as KafkaConsumer, KafkaException

from etl import logger


class Consumer(BaseModel):
    server: str = Field(..., title="Server")
    port: int = Field(..., title="Port")
    topic: str = Field(..., title="Topic")
    group_id: str = Field(..., title="Group ID")

    @property
    def conf(self) -> Dict[str, Any]:
        """
        Returns the configuration computed from the class
        """
        return {
            "bootstrap.servers": "{server}:{port}".format(
                server=self.server, port=self.port
            ),
            "group.id": self.group_id,
            "auto.offset.reset": "earliest",
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Creating consumer
        self.consumer = KafkaConsumer(self.conf)

        # Subscribe to topic
        self.consumer.subscribe([self.topic])

    def consume(self):
        """
        Reads the stream from the Kafka topic and returns the data.
        """
        msg = self.consumer.poll(1.0)
        if msg is None:
            return None
        if msg.error():
            logger.error("Consumer error: {}".format(msg.error()))
            raise KafkaException(msg.error())

        logger.debug("Received message: {}".format(msg.value().decode("utf-8")))
        return msg.value().decode("utf-8")

    def close(self):
        """
        Closes the consumer
        """
        self.consumer.close()
