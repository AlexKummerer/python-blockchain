blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction = [1]):
    blockchain.append([last_transaction,  transaction_amount])
    print(blockchain)


add_value(5.4)
add_value(0.1, get_last_blockchain_value())
add_value(49.3, get_last_blockchain_value())
