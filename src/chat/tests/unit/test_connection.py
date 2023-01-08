from multiprocessing.managers import SyncManager, ListProxy
import unittest
import unittest.mock
from unittest.mock import patch
from chat.client import Connection


class TestConnection(unittest.TestCase):
    def test_broadcast(self):
        with unittest.mock.patch.object(Connection, "connect"):
            c = Connection(("localhost", 9090))

        with unittest.mock.patch.object(c, "get_messages",
                                        return_value=[]):
            c.broadcast("some message")

            assert c.get_messages()[-1] == "some message"
