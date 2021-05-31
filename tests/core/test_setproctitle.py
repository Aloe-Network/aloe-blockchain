import unittest

from aloe.util.setproctitle import setproctitle


class TestSetProcTitle(unittest.TestCase):
    def test_does_not_crash(self):
        setproctitle("aloe test title")
