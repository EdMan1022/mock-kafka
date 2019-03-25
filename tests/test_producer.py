
import unittest

import confluent_kafka as ck

from mock_kafka import Producer


class TestProducer(unittest.TestCase):

    def setUp(self):
        self.producer = Producer({})

    def test_init(self):
        self.assertIsNotNone(self.producer)

    def test_list_topics(self):
        raise NotImplementedError

    def test_poll(self):
        raise NotImplementedError

    def test_produce(self):
        raise NotImplementedError

    def test_flush(self):
        raise NotImplementedError
