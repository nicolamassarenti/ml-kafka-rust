import unittest
from unittest.mock import patch


class TestSender(unittest.TestCase):
    @patch("data_generator.services.sender.KafkaProducer")
    def test_send(self, mock_kafka_producer):
        """
        Test that the send method calls the KafkaProducer
        """
        # Arrange
        from data_generator.services.sender import Sender

        image = b"fake image"
        endpoint = "fake endpoint"
        topic = "fake topic"

        # Act
        Sender.send(image, endpoint, topic)

        # Assert
        mock_kafka_producer.assert_called_once_with(bootstrap_servers=endpoint)
        mock_kafka_producer.return_value.send.assert_called_once_with(
            topic=topic, value=image
        )
        mock_kafka_producer.return_value.flush.assert_called_once()
