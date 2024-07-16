import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    criteria = {
        "Length (8 or more characters)": length_criteria,
        "Uppercase Letter": uppercase_criteria,
        "Lowercase Letter": lowercase_criteria,
        "Number": number_criteria,
        "Special Character": special_char_criteria
    }
    
    strength = sum(criteria.values())
    feedback = [f"{k}: {'✔️' if v else '❌'}" for k, v in criteria.items()]
    
    return strength, feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    
    print("\nPassword Strength Feedback:")
    for f in feedback:
        print(f)
    
    if strength == 5:
        print("\nPassword Strength: Strong")
    elif 3 <= strength < 5:
        print("\nPassword Strength: Medium")
    else:
        print("\nPassword Strength: Weak")

if __name__ == "__main__":
    main()
