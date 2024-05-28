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
    user_input = input(' Your choice: ')
    return user_input

def print_block():
    for block in blockchain:
        print("Outputting Block")
        print(block)
    
def verify_chain():
    """Verifies the integrity of the blockchain."""
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block[0] != blockchain[index - 1]:
            return False
    return True

def main():
    tx_amount = get_user_transaction()
    add_transaction(tx_amount, get_last_block())
    while True:
        print("Please choose")
        print('1: Add a new transaction value')
        print("2: Output the blockchain blocks")
        print("h: Manipulate the chain")
        print("3: Quit!")
        user_choice = get_user_choice()
        print(user_choice)   
        if user_choice == '1' :
            tx_amount = get_user_transaction()
            add_transaction(tx_amount, get_last_block())
        elif user_choice == '2':
            print_block()
        elif user_choice == 'h':
            if len(blockchain) >= 1:
                blockchain[0] = [2]
        elif user_choice == 'q':
            break
        else:
            print("Input was invalid, pls pick a value from the list!")
        if not verify_chain():
            print("Invalid blockchain")
            break
    print("Done")



if __name__ == "__main__":
    main()
4
