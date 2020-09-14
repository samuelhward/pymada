import pymada


def Event(name, *args, **kwargs):
    """
    """

    EVENTS = {}
    EVENTS["test_event"] = TestEvent

    return EVENTS[name](*args, **kwargs)


class BaseEvent:
    """
    """

    MESSAGE = "Event triggered!"

    @staticmethod
    @pymada.log(message=MESSAGE)
    def trigger():
        raise NotImplmentedError


class TestEvent(BaseEvent):
    """
    """

    MESSAGE = "test event triggered!"

    @staticmethod
    @pymada.log(message=MESSAGE)
    def trigger():
        pass
