import unittest
from unittest.mock import patch
from Services.UserService import UserService

class TestGetUserById(unittest.TestCase):
    @patch('your_module.User')  # Patch the 'User' class to mock the database query
    def test_get_userById_found(self, mock_user):
        # Set up the mock behavior
        user_instance = mock_user.query.filter_by.return_value.first.return_value
        user_instance.json.return_value = {'id': 1, 'name': 'John'}

        # Call the function being tested
        result = UserService.get_userById(1)

        # Check the expected result
        expected_result = {'The user was found': {'id': 1, 'name': 'John'}}
        self.assertEqual(result, expected_result)

    def test_get_userById_not_found(self):
        # Call the function being tested
        result = UserService.get_userById(2)

        # Check the expected result
        expected_result = {'message': 'The requested ID 2 was not found in the database'}
        self.assertEqual(result, expected_result)

    def test_get_userById_invalid_id(self):
        # Call the function being tested
        result = UserService.get_userById('invalid')

        # Check the expected result
        expected_result = {'message': 'The requested ID invalid was not found in the database'}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
