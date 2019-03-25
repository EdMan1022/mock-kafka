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
        :return:
        """
        with self.assertRaises(ValueError):
            Producer({"invalid-key": "invalid-value",
                      "bootstrap.servers": "test"})

    def test_list_topics(self):
        raise NotImplementedError

    def test_poll(self):
        raise NotImplementedError

    def test_produce(self):
        raise NotImplementedError

    def test_flush(self):
        raise NotImplementedError
