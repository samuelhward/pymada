import pymada.classes.event


def test_event():
    """"""

    test_event = pymada.classes.event.Event(name="test_event")
    test_event.trigger()
    with open(pymada.settings.logging_file_path) as file:
        assert any(test_event.MESSAGE in line for line in file.readlines())
