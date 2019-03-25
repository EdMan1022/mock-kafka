import confluent_kafka as ck


class Producer:
    """
    Mocks the Producer class which sends messages to Kafka brokers
    """

    # The full list of valid config keys for the producer
    # Not sure if all of these work, this is taken from a configuration
    # document for the underlying librdkafka C library,
    # so it's possible some of these aren't implemented correctly
    # with confluent-kafka
    valid_keys = (
        'bootstrap.servers',
        'builtin.features',
        'client.id',
        'metadata.broker.list',
        'message.max.bytes',
        'message.copy.max.bytes',
        'receive.message.max.bytes',
        'max.in.flight.requests.per.connection',
        'max.in.flight',
        'metadata.request.timeout.ms',
        'topic.metadata.refresh.interval.ms',
        'metadata.max.age.ms',
        'topic.metadata.refresh.fast.interval.ms',
        'topic.metadata.refresh.fast.cnt',
        'topic.metadata.refresh.sparse',
        'topic.blacklist',
        'debug',
        'socket.timeout.ms',
        'socket.blocking.max.ms',
        'socket.send.buffer.bytes',
        'socket.receive.buffer.bytes',
        'socket.keepalive.enable',
        'socket.nagle.disable',
        'socket.max.fails',
        'broker.address.ttl',
        'broker.address.family',
        'reconnect.backoff.jitter.ms',
        'reconnect.backoff.ms',
        'reconnect.backoff.max.ms',
        'statistics.interval.ms',
        'enabled_events',
        'error_cb',
        'throttle_cb',
        'stats_cb',
        'log_cb',
        'log_level',
        'log.queue',
        'log.thread.name',
        'log.connection.close',
        'background_event_cb',
        'socket_cb',
        'connect_cb',
        'closesocket_cb',
        'open_cb',
        'opaque',
        'default_topic_conf',
        'internal.termination.signal',
        'api.version.request',
        'api.version.request.timeout.ms',
        'api.version.fallback.ms',
        'broker.version.fallback',
        'security.protocol',
        'ssl.cipher.suites',
        'ssl.curves.list',
        'ssl.sigalgs.list',
        'ssl.key.location',
        'ssl.key.password',
        'ssl.certificate.location',
        'ssl.ca.location',
        'ssl.crl.location',
        'ssl.keystore.location',
        'ssl.keystore.password',
        'sasl.mechanisms',
        'sasl.mechanism',
        'sasl.kerberos.service.name',
        'sasl.kerberos.principal',
        'sasl.kerberos.kinit.cmd',
        'sasl.kerberos.keytab',
        'sasl.kerberos.min.time.before.relogin',
        'sasl.username',
        'sasl.password',
        'plugin.library.paths',
        'enable.idempotence',
        'enable.gapless.guarantee',
        'queue.buffering.max.messages',
        'queue.buffering.max.kbytes',
        'queue.buffering.max.ms',
        'linger.ms',
        'message.send.max.retries',
        'retries',
        'retry.backoff.ms',
        'queue.buffering.backpressure.threshold',
        'compression.codec',
        'compression.type',
        'batch.num.messages',
        'delivery.report.only.error',
        'dr_cb',
        'dr_msg_cb',
        'request.required.acks',
        'acks',
        'request.timeout.ms',
        'message.timeout.ms',
        'delivery.timeout.ms',
        'queuing.strategy',
        'produce.offset.report',
        'partitioner',
        'partitioner_cb',
        'msg_order_cmp',
        'opaque',
        'compression.codec',
        'compression.type',
        'compression.level'
    )

    def __init__(self, config):
        self._check_config(config)
        self._config = config
        self._cluster_metadata = None

    def _check_config(self, config):
        """
        Mimics how the real Producer behaves with it's config

        The real producer will fail when initialized without `bootstrap.servers`
        and if there are any invalid arguments in the config
        :param config: (dict) The config dictionary being checked
        :return: None
        """
        assert config['bootstrap.servers']

        invalid_keys = [
            key for key in config.keys()
            if key not in self.valid_keys
        ]
        if invalid_keys:
            raise ValueError(
                "The following keys are not supported by the config: {}".format(
                    invalid_keys))

    def configure_topic_metadata(self, topic_list, cluster_id=None,
                                 controller_id=-1, brokers=None, topics=None,
                                 orig_broker_id=None, orig_broker_name=None):
        """
        Allows the user to configure what the `list_topics` method returns
        :param topic_list:
        :param cluster_id:
        :param controller_id:
        :param brokers:
        :param topics:
        :param orig_broker_id:
        :param orig_broker_name:
        :return:
        """
        self._cluster_metadata = ck.admin.ClusterMetadata()
        self._cluster_metadata.cluster_id = cluster_id
        self._cluster_metadata.controller_id = controller_id
        self._cluster_metadata.brokers = brokers
        self._cluster_metadata.topics = topics
        self._cluster_metadata.orig_broker_id = orig_broker_id
        self._cluster_metadata.orig_broker_name = orig_broker_name

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

        Checks the incoming arguments for compatibility,
        raising the same error as the real Producer in the same situations

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

        if type(value) != bytes:
            raise ck.KafkaException(
                "The message value needs to be a bytes string, not type {}".format(
                    type(value)))
        return 0
