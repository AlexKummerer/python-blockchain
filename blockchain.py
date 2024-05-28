blockchain = []


def get_last_block():
    """Returns the last value in the blockchain if it exists, otherwise returns None."""
    return blockchain[-1] if blockchain else None


def add_transaction(transaction_amount, last_transaction=None):
    """Adds a new transaction to the blockchain."""
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


def get_user_transaction():
    """Prompts the user for a transaction amount and returns it as a float."""
    return float(input("Your transaction amount please: "))


def main():
    for _ in range(3):
        tx_amount = get_user_transaction()
        add_transaction(tx_amount, get_last_block())


if __name__ == "__main__":
    main()
