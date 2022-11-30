import io

import numpy as np

from typing import Tuple
from PIL import Image


class Transformer:
    @staticmethod
    def transform(message, image_size: Tuple[int, int]) -> np.ndarray:
        """
        Transform the message from kafka. More specifically, it resizes the image to `IMAGE_SIZE`
        and converts it to a numpy array.
        """
        # Decode the message
        image = Image.open(io.BytesIO(message))

        # Resize the image
        image = image.resize(image_size)

        # Convert the image to a numpy array
        image = np.array(image)

        # Return the image
        return image
