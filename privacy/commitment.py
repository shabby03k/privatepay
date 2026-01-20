import random
from .hash_utils import hash_data

def create_commitment(amount):
    secret = random.randint(100000, 999999)
    commitment = hash_data(f"{amount}{secret}")
    return commitment, secret
