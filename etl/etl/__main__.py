import os
import typer

from etl import logger
from etl.services import Consumer, Transformer, Loader

app = typer.Typer()


@app.command()
def consume(
    server: str = typer.Option(
        ..., help="The url of the Kafka server", envvar=["KAFKA_SERVER"]
    ),
    port: int = typer.Option(..., help="The Kafka port", envvar=["KAFKA_PORT"]),
    topic: str = typer.Option(..., help="The topic to consume", envvar=["KAFKA_TOPIC"]),
    group_id: str = typer.Option(..., help="The group ID", envvar=["KAFKA_GROUP_ID"]),
):
    IMAGE_HEIGHT = os.getenv("IMAGE_HEIGHT")
    IMAGE_WIDTH = os.getenv("IMAGE_WIDTH")
    IMAGE_SIZE = (IMAGE_HEIGHT, IMAGE_WIDTH)
    logger.info(f"IMAGE_SIZE: {IMAGE_SIZE}")

    consumer = Consumer(
        server=server,
        port=port,
        topic=topic,
        group_id=group_id,
    )

    while os.getenv("CONSUMER_RUNNING", None):
        logger.debug("Reading from Kafka")
        message = consumer.consume()
        if message:
            logger.debug("Message received: {}".format(message))
        else:
            logger.debug("No message received")

    consumer.close()
    pass


if __name__ == "__main__":
    app()
