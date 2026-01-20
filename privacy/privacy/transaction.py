from .hash_utils import hash_data
from .commitment import create_commitment

class PrivateTransaction:
    def __init__(self, sender, receiver, amount):
        self.sender_hash = hash_data(sender)
        self.receiver = receiver
        self.commitment, self.secret = create_commitment(amount)

    def verify(self, amount, secret):
        return self.commitment == hash_data(f"{amount}{secret}")
