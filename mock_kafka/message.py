import confluent_kafka as ck

class Message:
    """
    Mocks the confluent-kafka `Message` class

    This class will be used by the mock producer and consumer classes,
    and will allow the user to make messages with set test data
    """

    def __init__(self, value=None, topic=None, headers=None, key=None,
                 error=None, partition=None, offset=None, create_time=None, log_time=None):
        self._value = value
        self._topic = topic
        self._headers = headers
        self._key = key
        self._kafka_error = None
        self._partition = partition
        self._offset = offset
        self._timestamp = None
        self._timestamp_type = ck.TIMESTAMP_NOT_AVAILABLE

        if create_time:
            self._timestamp = create_time
            self._timestamp_type = ck.TIMESTAMP_CREATE_TIME
            if log_time:
                raise ValueError("You can't have a log and create time")
        if log_time:
            if create_time:
                raise ValueError("You can't have a log and create time")
            self._timestamp = log_time
            self._timestamp_type = ck.TIMESTAMP_LOG_APPEND_TIME

        if error:
            self._kafka_error = ck.KafkaException(
                'Error manually set by init flag')

    def error(self):
        """
        If _kafka_error is an error, raises it
        """
        if self._kafka_error:
            raise self._kafka_error

    def key(self):
        """
        Getter method for the key attribute
        """
        return self._key

    def set_key(self, key):
        self._key = key

    def value(self):
        """
        Gets the value attribute
        """
        return self._value

    def set_value(self, value):
        self._value = value

    def set_headers(self, headers):
        self._headers = headers

    def headers(self):
        return self._headers

    def partition(self):
        """
        The number of the partition the message is from or None if not available
        :return: int or None
        """
        return self._partition

    def topic(self):
        """
        Gets the topic name for the message or None if not available

        :return: str or None
        """
        return self._topic

    def offset(self):
        """
        Gets the offset of the message in the topic
        :return: int or None
        """
        return self._offset

    def timestamp(self):
        return self._timestamp_type, self._timestamp

