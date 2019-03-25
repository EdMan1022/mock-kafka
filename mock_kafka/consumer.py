class Consumer:
    """
    Mocks the Consumer class which pulls messages from Kafka brokers
    """

    def __init__(self):
        raise NotImplementedError

    def assign(self):
        raise NotImplementedError

    def assignment(self):
        raise NotImplementedError

    def commit(self):
        raise NotImplementedError

    def committed(self):
        raise NotImplementedError

    def consume(self):
        raise NotImplementedError

    def get_watermark_offsets(self):
        raise NotImplementedError

    def list_topics(self):
        raise NotImplementedError

    def offsets_for_times(self):
        raise NotImplementedError

    def pause(self):
        raise NotImplementedError

    def poll(self):
        raise NotImplementedError

    def position(self):
        raise NotImplementedError

    def resume(self):
        raise NotImplementedError

    def seek(self):
        raise NotImplementedError

    def store_offsets(self):
        raise NotImplementedError

    def subscribe(self):
        raise NotImplementedError

    def unassign(self):
        raise NotImplementedError

    def unsubscribe(self):
        raise NotImplementedError

