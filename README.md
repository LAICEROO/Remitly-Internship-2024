# IAM Role Policy Verifier
This Python script verifies IAM role policies according to the specified criteria. It checks if the Resource field in the IAM policy contains a single asterisk. If it does, the verification returns False; otherwise, it returns True.

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/LAICEROO/Remitly_Intership_2024.git
    ```
2. Navigate to the directory containing the script:
    ```bash
    cd iam_role_verification
    ```
3. Run the script:
    ```bash
    python iam_role_policy_verifier.py AWS_ROLE.json
    ```

## Unit Tests
You can run the unit tests using the following command:
    ```bash
    python -m unittest test_iam_verification.py
    ```
    
## File Structure
iam_role_verification.py: Contains the main script for verifying IAM role policies.
test_iam_role_verification.py: Contains unit tests for the verification function.
README.md: This README file.

## Dependencies
- Python 3.x
- unittest module 
