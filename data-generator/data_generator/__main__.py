import time
import typer
import base64
import requests
import os

from data_generator import logger, Sender


app = typer.Typer(name="data-generator")


@app.command()
def from_url(
    url: str = typer.Option(
        ...,
        help="The url from which to download the data",
        envvar="URL",
        show_envvar=True,
    ),
    sleep: int = typer.Option(
        ...,
        help="The delay between two data generations",
        envvar="SLEEP",
        show_envvar=True,
    ),
    endpoint: str = typer.Option(
        ...,
        help="The recipient of the generated data",
        envvar="ENDPOINT",
        show_envvar=True,
    ),
):
    """
    Generates data from a URL and sends it to the endpoint using Kafka
    :param url: the url from which to download the data
    :param sleep: the delay between two data generations
    :param endpoint: the recipient of the generated data
    :return: None
    """
    logger.info(
        "from-url - 'url': '{url}, 'sleep': {sleep}, 'endpoint': {endpoint}".format(
            url=url, sleep=sleep, endpoint=endpoint
        )
    )

    while True:
        # Downloading image from url and converting it to base64
        image = base64.b64encode(requests.get(url).content)

        logger.info("Sending image to url '{endpoint}'".format(endpoint=endpoint))
        # Sending image to endpoint
        Sender.send(image=image, endpoint=endpoint, topic=os.getenv("TOPIC"))

        logger.info("Sleeping {x}ms".format(x=sleep))
        # Sleeping `sleep` milliseconds
        time.sleep(sleep / 1000)


@app.command()
def from_scraping(name: str):
    """
    Performs scarping from `url` using the query `query` and sends the data to `endpoint` every `sleep` milliseconds
    """
    pass


if __name__ == "__main__":
    app()
