# Data generator

## In a nutshell
This is a simple data generator that retrieves data from the web and publishes it to a Kafka topic.

## How to run it
You can run this package either with Docker or with Python.

### Docker
To run the data generator with Docker, you need to have Docker installed on your machine. Then, you can run the following command:

```bash
./docker/devops/run.sh
```

This will build the Docker image. Then, you can run the following command to run the data generator:

```bash
URL="www.your-target-url.com/something" # The URL to retrieve data from
SLEEP=10 # in milliseconds
ENDPOINT="127.something.x.y:1234" # the endpoint to publish to
TOPIC="some-topic" # the topic to publish to

./docker/devops/run.sh ${URL} ${SLEEP} ${ENDPOINT} ${TOPIC}
```
where:
- `URL` is the URL to retrieve data from
- `SLEEP` is the time to wait between each request
- `ENDPOINT` is the endpoint to publish to
- `TOPIC` is the topic to publish to

### Python
To run the data generator with Python, you need to have Python >= 3.7 installed on your machine. Then, you can run the following command:

```bash
poetry config virtualenvs.in-project true && \
poetry install  --no-dev  && \
poetry run -m data_generator from-url --url "${URL}" \
                                      --sleep "${SLEEP}" \
                                      --endpoint "${ENDPOINT}" && \
rm -r --force .venv   # Clean up
```
