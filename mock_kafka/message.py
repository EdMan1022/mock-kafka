from confluent_kafka import KafkaException

class Message:
    """
    Mocks the confluent-kafka `Message` class

    This class will be used by the mock producer and consumer classes,
    and will allow the user to make messages with set test data
    """

    def __init__(self, value=None, topic=None, headers=None, key=None, error=None):
        self._value = value
        self._topic = topic
        self._headers = headers
        self._key = key
        self._kafka_error = None

        if error:
            self._kafka_error = KafkaException('Error manually set by init flag')


    def error(self):
        """
        If _kafka_error is an error, raises it
        """
        if self._kafka_error:
            raise self._kafka_error

