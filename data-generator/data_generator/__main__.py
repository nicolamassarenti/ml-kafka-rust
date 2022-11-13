import time
import typer
import base64
import requests

from data_generator import logger, Sender


app = typer.Typer(name="data-generator")


@app.command()
def from_url(
    url: str = typer.Argument(..., help="The url from which to download the data", envvar="URL", show_envvar=True),
    sleep: int = typer.Argument(..., help="The delay between two data generations", envvar="SLEEP", show_envvar=True),
    endpoint: str = typer.Argument(
        ..., help="The recipient of the generated data", envvar="ENDPOINT", show_envvar=True
    ),
):
    """
    Retrieves an image from `url` and sends it to `endpoint` every `sleep` milliseconds
    """
    logger.info(
        "from-url - 'url': '{url}, 'sleep': {sleep}, 'endpoint': {endpoint}".format(
            url=url, sleep=sleep, endpoint=endpoint
        )
    )
    # Downloading image from url and converting it to base64
    image = base64.b64encode(requests.get(url).content)

    logger.info("Sending image to url '{endpoint}'".format(endpoint=endpoint))
    # Sending image
    Sender.send(image=image, endpoint=endpoint)

    logger.info("Sleeping {x}ms".format(x=sleep))
    # Sleeping `sleep` milliseconds
    time.sleep(sleep)


@app.command()
def from_scraping(name: str):
    """
    Performs scarping from `url` using the query `query` and sends the data to `endpoint` every `sleep` milliseconds
    """
    pass

if __name__ == "__main__":
    app()
