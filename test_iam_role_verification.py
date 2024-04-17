import unittest
import iam_role_verification

# Unit tests
class TestVerifyIAMRolePolicy(unittest.TestCase):
    # Test case for a valid input JSON file
    def test_valid_input(self):
        input_json_file = "valid_aws_role.json"
        self.assertTrue(iam_role_verification.verify(input_json_file))

    # Test case for an invalid input JSON file
    def test_invalid_input(self):
        input_json_file = "invalid_aws_role.json"
        self.assertFalse(iam_role_verification.verify(input_json_file))

    # Test case for a non-existent input JSON file
    def test_file_not_found(self):
        input_json_file = "nonexistent_file.json"
        self.assertFalse(iam_role_verification.verify(input_json_file))

    # Test case for an input JSON file with invalid JSON format
    def test_invalid_json_format(self):
        input_json_file = "invalid_json_format.json"
        self.assertFalse(iam_role_verification.verify(input_json_file))

if __name__ == '__main__':
    unittest.main()
