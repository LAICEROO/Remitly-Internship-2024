import json

# Function to verify IAM role policy
def verify(input_json_file):
    try:
        # Open the input JSON file
        with open(input_json_file, 'r') as file:
            data = json.load(file)

            # Check if Resource field contains a single asterisk
            if 'Resource' in data['PolicyDocument']['Statement'][0]:
                resource_value = data['PolicyDocument']['Statement'][0]['Resource']
                if resource_value == '*':
                    return False
            return True
    except FileNotFoundError:
        # Handle file not found error
        print("File not found.")
        return False
    except (json.JSONDecodeError, KeyError, IndexError):
        # Handle JSON decode error or missing required fields
        print("Invalid JSON format or missing required fields.")
        return False
