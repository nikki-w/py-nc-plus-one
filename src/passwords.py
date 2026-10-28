import os
import bcrypt

def hash_password(password: str) -> str:
    # Minimum cost in tests keeps the per-test reseed test (make salting less for tests basically)
    rounds = 4 if os.getenv("ENV") == "test" else 12
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds)).decode()

def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password.encode())