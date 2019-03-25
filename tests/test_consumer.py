import unittest

import confluent_kafka as ck

from mock_kafka import Consumer


class TestConsumer(unittest.TestCase):
    """
    Tests functionality for the mock Consumer class
    """

    def setUp(self):
        self.consumer = Consumer({'bootstrap.servers': 'test'})

    def test_init(self):
        self.assertIsNotNone(self.consumer)

    def test_assign(self):
        raise NotImplementedError

    def test_assignment(self):
        raise NotImplementedError

    def test_close(self):
        raise NotImplementedError

    def test_commit(self):
        raise NotImplementedError

    def test_committed(self):
        raise NotImplementedError

    def test_consume(self):
        raise NotImplementedError

    def test_get_watermark_offsets(self):
        raise NotImplementedError

    def test_list_topics(self):
        raise NotImplementedError

    def test_offsets_for_times(self):
        raise NotImplementedError

    def test_pause(self):
        raise NotImplementedError

    def test_poll(self):
        raise NotImplementedError

    def test_position(self):
        raise NotImplementedError

    def test_resume(self):
        raise NotImplementedError

    def test_seek(self):
        raise NotImplementedError

    def test_store_offsets(self):
        raise NotImplementedError

    def test_subscribe(self):
        raise NotImplementedError

    def test_unassign(self):
        raise NotImplementedError

    def test_unsubscribe(self):
        raise NotImplementedError
