## Overview
This is a package containing mock versions of pieces of `confluent-kafka`,
a python package that serves as a wrapper for a fast C library
used to interact with the brokers of a Kafka cluster.
These mock classes mimic the interface of the real objects,
in addition to having methods that make it easy for the user to specify
particular behavior that a given object should have,
like returning a specific message when called.
This should make writing unit tests possible.
