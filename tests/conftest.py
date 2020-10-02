"""tests/conftest.py"""


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    def noop(*args):
        return

    terminalreporter.short_test_summary = noop
