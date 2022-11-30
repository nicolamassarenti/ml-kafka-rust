import requests


class Inferencer:
    @staticmethod
    def infer(data, schema):
        """
        Makes a REST request to the inferencer service and returns the inferred result.
        """
        # Prepare payload
        payload = {"data": data, "schema": schema}

        # Make request
        response = requests.post(
            url="{server}:{port}/infer".format(
                server=INFERENCER_SERVER, port=INFERENCER_PORT
            ),
            json=payload,
        )

        # Check response
        if response.status_code != 200:
            raise Exception("Inferencer error: {}".format(response.text))

        # Return result
        return response.json()
