import unittest

import confluent_kafka

from mock_kafka import Message


class TestMessage(unittest.TestCase):
    """
    Tests functionality of the class that mocks kafka messages

    Many of the methods that are being tested are basically getters for
    attributes stored directly on the class, which looks weird,
    but the real `Message` class uses this interface, so this is copying it.
    (The real message probably uses getters because it's written in C,
    and may not actually have the attributes on it like a normal
    python object)
    """

    def setUp(self):
        self.message = Message(
                value=b'test-value',
                topic='test-topic',
                headers=(
                        ('test-header-key-1', 'test-header-value-1'),
                        ('test-header-key-2', 'test-header-value-2')
                        ),
                key='test-key'
            )

    def test_init(self):
        self.assertIsNotNone(self.message)

    def test_key_method(self):
        self.assertEqual('test_key', self.message.key())

    def test_no_error(self):
        self.assertIsNone(self.message.error())

    def test_error(self):
        message = Message(error=True)

        with self.assertRaises(confluent_kafka.KafkaException):
            message.error()

    def test_headers(self):
        self.assertTupleEqual(
                self.message.headers(),
                (
                    ('test-header-key-1', 'test-header-value-1'),
                    ('test-header-key-2', 'test-header-value-2')
                )
            )

    def test_offset(self):
        raise NotImplementedError

    def test_partition(self):
        raise NotImplementedError

    def test_set_headers(self):
        raise NotImplementedError

    def test_set_key(self):
        raise NotImplementedError

    def test_set_value(self):
        raise NotImplementedError

    def test_timestamp(self):
        raise NotImplementedError

    def test_topic(self):
        raise NotImplementedError

    def test_value(self):
        raise NotImplementedError

