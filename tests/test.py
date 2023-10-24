import string
import random
import hashlib

class PasswordChecker:
    def __init__(self):
        self.password_history = {}
        self.common_passwords = ['password', '123456', 'admin', 'qwerty', 'secret', 'letmein', 'dragon', 'baseball', 'football', 'iloveyou', 'password1', 'password2', 'password3', 'password4', 'password5', 'password6', 'password7', 'password8', 'password9', 'password10']

    def check_password_strength(self, password):
        # check password against hash of common passwords
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password in self.common_passwords:
            return "Very Weak"

        # check password length
        if len(password) < 8:
            return "Very Weak"

        # check password complexity
        complexity = [ch.isdigit() for ch in password] + \
                     [ch.isalpha() for ch in password] + \
                     [ch in string.punctuation for ch in password]

        if complexity.count(True) < 3:
            return "Weak"

        if len(password) >= 12:
            return "Strong"

        if len(password) >= 10:
            return "Moderate"

        return "Very Weak"

    def generate_password(self, length=8):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for i in range(length))
        return password

    def get_password_history(self):
        return self.password_history

    def start(self):
        while True:
            user_input = input("Press 'c' to check a password, 'g' to generate a password, 'h' to view password history, or 'q' to quit: ")

            if user_input.lower() == 'c':
                password = input("Enter your password: ")
                strength = self.check_password_strength(password)
                print(f"The strength of your password is: {strength}")

            elif user_input.lower() == 'g':
                length = int(input("Enter the desired password length (default 8): ") or 8)
                password = self.generate_password(length)
                print(f"Generated password: {password}")
                strength = self.check_password_strength(password)
                print(f"The strength of the generated password is: {strength}")

            elif user_input.lower() == 'h':
                print("Password history:")
                for password, strength in self.password_history.items():
                    print(f"Password: {password}, Strength: {strength}")

            elif user_input.lower() == 'q':
                break

            else:
                print("Invalid input. Please try again.")

checker = PasswordChecker()
checker.start()