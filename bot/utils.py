import secrets

def generate_code():
    number = "1234567890"
    return ''.join(secrets.choice(number) for _ in range(6))