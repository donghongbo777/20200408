import pytest
import requests
from unittest.mock import patch

# Import the function to be tested
from jiguanjuofflinedev import devops


class Test_JiguanjuofflinedevDevops:

    def test_send_text_message_success(self):
        # Test data
        sendmsg = "Test message"

        # Mocking the requests.post method
        with patch('requests.post') as mock_post:
            devops(sendmsg)

            # Assert that requests.post was called with the correct arguments
            mock_post.assert_called_once_with('https://qyapi.weixin.qq.com/cgi-bin/webhook/send',
                                              headers={'Content-Type': 'application/json'},
                                              params=(('key', 'acb620de-ddd0-4128-b79a-33ae814f2659'),),
                                              data='{"msgtype": "text","text": {"content": "Test message"}}')

    def test_send_empty_message(self):
        # Test data
        sendmsg = ""

        # Mocking the requests.post method
        with patch('requests.post') as mock_post:
            devops(sendmsg)

            # Assert that requests.post was called with the correct arguments
            mock_post.assert_called_once_with('https://qyapi.weixin.qq.com/cgi-bin/webhook/send',
                                              headers={'Content-Type': 'application/json'},
                                              params=(('key', 'acb620de-ddd0-4128-b79a-33ae814f2659'),),
                                              data='{"msgtype": "text","text": {"content": ""}}')

    def test_send_message_with_special_characters(self):
        # Test data
        sendmsg = "Special characters: 😊🚀"

        # Mocking the requests.post method
        with patch('requests.post') as mock_post:
            devops(sendmsg)

            # Assert that requests.post was called with the correct arguments
            mock_post.assert_called_once_with('https://qyapi.weixin.qq.com/cgi-bin/webhook/send',
                                              headers={'Content-Type': 'application/json'},
                                              params=(('key', 'acb620de-ddd0-4128-b79a-33ae814f2659'),),
                                              data='{"msgtype": "text","text": {"content": "Special characters: 😊🚀"}}')

    def test_send_message_network_failure(self):
        # Test data
        sendmsg = "Network failure message"

        # Mocking the requests.post method to raise a ConnectionError
        with patch('requests.post', side_effect=requests.ConnectionError):
            with pytest.raises(requests.ConnectionError):
                devops(sendmsg)
