""" Module for acceptance test of chat app """
from multiprocessing.managers import SyncManager, ListProxy
import unittest
import unittest.mock

from chat.client import ChatClient
from chat.server import new_chat_server


class TestChatAcceptance(unittest.TestCase):
    """ Class testing application qualifications"""

    def test_message_exchange(self):
        """ Tests if message exchange through """
        with new_chat_server():
            user1 = ChatClient("John Doe")
            user2 = ChatClient("Harry Potter")

            user1.send_message("Hello World")
            messages = user2.fetch_messages()

            assert messages == ["John Doe: Hello World"]


    def test_smoke_sending_message(self):
        with new_chat_server():
            user1 = ChatClient("User1")
            user1.send_message("Hello World")

# class TestChatMultiUser(unittest.TestCase):
#     """ Test suite for multiple users """

#     def test_many_users(self):
#         """ Test commincations between multiple users """
#         with new_chat_server():
#             first_user = ChatClient("John Doe")
#             for uid in range(5):
#                 moreuser = ChatClient(f"User {uid}")
#                 moreuser.send_message("Hello!")

#             messages = first_user.fetch_messages()
#             assert len(messages) == 5

#     def test_multiple_readers(self):
#         """ Verify that all users in the chat see the same exact messages """
#         with new_chat_server():
#             user1 = ChatClient("John Doe")
#             user2 = ChatClient("User 2")
#             user3 = ChatClient("User 3")

#             user1.send_message("Hi all")
#             user2.send_message("Hello World")
#             user3.send_message("Hi")

#             user1_messages = user1.fetch_messages()
#             user2_messages = user2.fetch_messages()
#             self.assertEqual(user1_messages, user2_messages)


# _messages = []


# def _srv_get_messages():
#     return _messages


# class _ChatServerManager(SyncManager):
#     pass


# _ChatServerManager.register("get_messages",
#                             callable=_srv_get_messages,
#                             proxytype=ListProxy)


# def new_chat_server():
#     """ Created new server for the chat """
#     return _ChatServerManager(("", 9090), authkey=b'mychatsecret')
