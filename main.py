import re

# Function to evaluate password strength
def evaluate_password_strength(password):
    length = len(password)
    strength = 0

    # Check for minimum length
    if length >= 8:
        strength += 1
    else:
        return "Very Weak"

    # Check for at least one uppercase letter
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for at least one lowercase letter
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for at least one digit
    if re.search(r"\d", password):
        strength += 1

    # Check for at least one special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Determine the strength based on the criteria
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Medium"
    elif strength == 2:
        return "Weak"
    else:
        return "Very Weak"

# Main function to interact with the user
def main():
    password = input("Enter a password to check its strength: ")
    strength = evaluate_password_strength(password)
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
