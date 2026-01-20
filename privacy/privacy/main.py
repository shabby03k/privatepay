from privacy.transaction import PrivateTransaction

tx = PrivateTransaction(
    sender="AliceWallet123",
    receiver="BobWallet456",
    amount=50
)

print("Sender Hidden:", tx.sender_hash)
print("Receiver:", tx.receiver)
print("Amount Commitment:", tx.commitment)
