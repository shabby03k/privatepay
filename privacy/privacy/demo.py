from privacy.transaction import PrivateTransaction

tx = PrivateTransaction("Alice", "Bob", 100)

print("Transaction Valid:", tx.verify(100, tx.secret))
