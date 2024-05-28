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

def get_user_choice():
    user_input = int(input(' Your choice: '))
    return user_input

def print_block():
    for block in blockchain:
        print("Outputting Block")
        print(block)
    

def main():
    tx_amount = get_user_transaction()
    add_transaction(tx_amount, get_last_block())
    while True:
        print("Please choose")
        print('1: Add a new transaction value')
        print("2: Output the blockchain blocks")
        user_choice = get_user_choice()
        print(user_choice)   
        if user_choice == 1 :
            tx_amount = get_user_transaction()
            add_transaction(tx_amount, get_last_block())
        elif user_choice == 2:
            print_block()
        else:
            print("Input was invalid, pls pick a value from the list!")



if __name__ == "__main__":
    main()
4
