class Producer:
    """
    Mocks the Producer class which sends messages to Kafka brokers
    """

    def __init__(self, config):
        self._config = config

    def len(self):
        """
        Gets the number of messages/protocol requests waiting to be delivered to the broker
        :return: int
        """
        raise NotImplementedError

    def flush(self, timeout=None):
        """
        Waits for all messages in the Producer's queue to be delivered

        Calls poll until the len parameter is 0 or the timeout elapses
        Returns len() at the end of the operation
        :param timeout: (float) Optional seconds before timeout
        :return: (int) The number of messages remaining in the queue
        """
        raise NotImplementedError

    def list_topics(self, topic=None, timeout=-1):
        """
        Requests metadata from the cluster about the topics

        If a topic is provided then only metadata about that topic is returned
        The timeout is an optional timeout for the request
        :param topic: (str) Optional topic to limit request to
        :param timeout: (float) Max seconds before timing out, -1 for no timeout
        :return: ClusterMetadata
        """
        raise NotImplementedError

    def poll(self, timeout):
        """
        Polls the producer for events and calls the corresponding callback

        :param timeout: (float) seconds before timeout
        :return: (int) The number of events processed
        """
        raise NotImplementedError

    def produce(self, topic, value, key, partition=None, on_delivery=None,
                timestamp=None, headers=None):
        """
        Mocks producing a message to a topic

        :param topic: (str) Topic to produce message to
        :param value: (str|bytes) Message payload
        :param key: (str|bytes) Message key
        :param partition: (int) Optionally specify partition (otherwise uses
                                built in partitioner)
        :param on_delivery: (func) Delivery report callback to call (err, msg)
        :param timestamp: (int) Unix timestamp to add to the message
        :param headers: (dict) Message headers
        :return: None
        """
        raise NotImplementedError
