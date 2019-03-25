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
        self.assertEqual('test-key', self.message.key())

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
        message = Message(offset=1)
        self.assertEqual(message.offset(), 1)

    def test_partition(self):
        message = Message(partition=1)
        self.assertEqual(message.partition(), 1)

    def test_set_headers(self):
        self.message.set_headers(
            (
                ('new-header-key-1', 'new-header-value-1'),
                ('new-header-key-2', 'new-header-value-2')
            ))
        self.assertEqual(self.message._headers,
                         (
                             ('new-header-key-1', 'new-header-value-1'),
                             ('new-header-key-2', 'new-header-value-2')
                         )
                         )

    def test_set_key(self):
        self.message.set_value('new-key')
        self.assertEqual(self.message._value, 'new-key')

    def test_set_value(self):
        self.message.set_value(b'some-new-value')
        self.assertEqual(self.message._value, b'some-new-value')

    def test_create_timestamp(self):
        message = Message(create_time=1553527487)
        self.assertTupleEqual(
            message.timestamp(),
            (confluent_kafka.TIMESTAMP_CREATE_TIME, 1553527487)
        )

    def test_timestamp_not_available(self):
        message = self.message

        self.assertTupleEqual(
            message.timestamp(),
            (confluent_kafka.TIMESTAMP_NOT_AVAILABLE, None)
        )

    def test_log_timestamp(self):
        message = Message(log_time=1553527487)
        self.assertTupleEqual(
            message.timestamp(),
            (confluent_kafka.TIMESTAMP_LOG_APPEND_TIME, 1553527487)
        )

    def test_topic(self):
        self.assertEqual(self.message.topic(), 'test-topic')

    def test_value(self):
        self.assertEqual(self.message.value(), b'test-value')
