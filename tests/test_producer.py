import unittest

import confluent_kafka as ck

from mock_kafka import Producer


class TestProducer(unittest.TestCase):

    def setUp(self):
        self.producer = Producer({'bootstrap.servers': 'test'})

    def test_init(self):
        self.assertIsNotNone(self.producer)

    def test_no_bootstrap_server(self):
        """
        Init should fail with no bootstrap.servers key in config
        :return:
        """
        with self.assertRaises(KeyError):
            Producer({'client.id': 'test'})

    def test_invalid_config_keys(self):
        """
        Tests the config checking that occurs on init
        :return: None
        """
        with self.assertRaises(ValueError):
            Producer({"invalid-key": "invalid-value",
                      "bootstrap.servers": "test"})

    def test_list_all_topics(self):
        """
        After setting topic metadata, list_topics should return metadata object
        :return: None
        """
        self.producer.configure_topic_metadata(
            topic_list=['test-topic-1', 'test-topic-2'])

        cluster_metadata = self.producer.list_topics()

        self.assertEqual(cluster_metadata.cluster_id, None)
        self.assertEqual(
            cluster_metadata.topics[0].topic,
            'test-topic-1'
        )

        raise NotImplementedError

    def test_poll(self):
        """
        Calling the poll method manually without callbacks returns 0
        :return: None
        """
        output = self.producer.poll(1)
        self.assertEqual(output, 0)

    def test_produce(self):
        """
        Calling produce with correct formatting shouldn't raise errors
        :return: None
        """
        self.producer.produce(
            'test-topic',
            b'test-value',
            'test-key'
        )

    def test_produce_incorrect_value(self):
        """
        Calling produce with a string instead of a bytestring should fail
        :return: None
        """
        with self.assertRaises(ck.KafkaException):
            self.producer.produce(
                'test-topic',
                'test-value',
                'test-key'
            )

    def test_flush(self):
        """
        Flush should return 0 if it isn't configured to time out
        :return: None
        """

        output = self.producer.flush(1)

        self.assertEqual(
            output,
            0
        )
