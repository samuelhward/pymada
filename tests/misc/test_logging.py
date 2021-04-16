import pymada.settings


def test_logging():
    """"""

    assert pymada.settings.debug_mode is True
    log_message = "porkins!"
    pymada.logger.info(log_message)
    with open(pymada.settings.logging_file_path) as file:
        assert f"pymada_log INFO: {log_message}\n" in file.readlines()
