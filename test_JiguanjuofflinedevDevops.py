import pytest
import requests
from unittest.mock import patch

# Import the function to be tested
from jiguanjuofflinedev import devops

class Test_JiguanjuofflinedevDevops:
    
    def test_send_text_message_success(self):
        # Arrange
        valid_message = "Test message"
        
        # Act
        with patch('requests.post') as mock_post:
            devops(valid_message)
        
        # Assert
        mock_post.assert_called_once()
    
    def test_send_empty_message(self):
        # Arrange
        empty_message = ""
        
        # Act
        with patch('requests.post') as mock_post:
            devops(empty_message)
        
        # Assert
        mock_post.assert_called_once()
    
    def test_send_message_with_special_characters(self):
        # Arrange
        special_message = "Special characters: 😊"
        
        # Act
        with patch('requests.post') as mock_post:
            devops(special_message)
        
        # Assert
        mock_post.assert_called_once()
    
    def test_send_message_network_failure(self):
        # Arrange
        network_failure_message = "Network failure message"
        
        # Act
        with patch('requests.post') as mock_post:
            # Simulate network failure by raising an exception
            mock_post.side_effect = requests.exceptions.RequestException
            
            # Assert
            with pytest.raises(requests.exceptions.RequestException):
                devops(network_failure_message)

