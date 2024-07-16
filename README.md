# PRODIGY_CS_03
# # Password Strength Checker

This Python script checks the strength of a password based on various criteria such as length, presence of uppercase and lowercase letters, digits, special characters, and whether the password is common or not.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies listed in the `requirements.txt` file using `pip install -r requirements.txt`.
3. Run the `password_strength_checker.py` script.
4. You will be prompted to enter a password.
5. The script will analyze the password and provide feedback on its strength based on the defined criteria.

## Functions

- `get_common_passwords_list()`: Retrieves a list of common passwords from a URL.
- `check_password_strength(password, common_passwords)`: Checks the strength of the provided password against defined criteria and provides feedback.

## Example

```python
common_passwords_list = get_common_passwords_list()

# Ask the user for their password
user_password = input("Enter your password: ")
check_password_strength(user_password, common_passwords_list)
