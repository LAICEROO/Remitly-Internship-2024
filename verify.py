import unittest
import json

# Function to verify IAM role policy
def verify(input_json_file):
    try:
        with open(input_json_file, 'r') as file:
            data = json.load(file)

            # Check if Resource field contains a single asterisk
            if 'Resource' in data['PolicyDocument']['Statement'][0]:
                resource_value = data['PolicyDocument']['Statement'][0]['Resource']
                if resource_value == '*':
                    return False
            return True
    except FileNotFoundError:
        print("File not found.")
        return False
    except (json.JSONDecodeError, KeyError, IndexError):
        print("Invalid JSON format or missing required fields.")
        return False


# Unit tests
class TestVerifyIAMRolePolicy(unittest.TestCase):
    def test_valid_input(self):
        input_json_file = "valid_aws_role.json"
        self.assertTrue(verify(input_json_file))

    def test_invalid_input(self):
        input_json_file = "invalid_aws_role.json"
        self.assertFalse(verify(input_json_file))

    def test_file_not_found(self):
        input_json_file = "nonexistent_file.json"
        self.assertFalse(verify(input_json_file))

    def test_invalid_json_format(self):
        input_json_file = "invalid_json_format.json"
        self.assertFalse(verify(input_json_file))

if __name__ == '__main__':
    unittest.main()
