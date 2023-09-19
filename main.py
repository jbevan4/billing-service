from operator import add, sub
from billing_service.domain.wallet.wallet import Wallet
from billing_service.domain.wallet.events import WalletCreated, BalanceChanged
from billing_service.domain.wallet.repository import Repository


def main():
    repository = Repository()

    while True:
        print("1. Create Wallet")
        print("2. Change Balance")
        print("3. View Wallet")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            wallet = repository.get(user_id)
            repository.save(wallet=wallet)
            print("Wallet created successfully!")
        elif choice == "2":
            user_id = input("Enter user ID: ")
            wallet = repository.get(user_id)
            if not wallet:
                print("Wallet not found!")
                continue
            amount = int(input("Enter amount to change: "))
            operation = add if amount >= 0 else sub
            amount = abs(amount)
            wallet.handle_balance_changed(BalanceChanged(wallet.id, amount, operation))
            repository.save(wallet)
            print("Balance changed successfully!")
        elif choice == "3":
            user_id = input("Enter user ID: ")
            wallet = repository.get(user_id)
            if not wallet:
                print("Wallet not found!")
                continue
            print(f"Wallet ID: {wallet.id}")
            print(f"Events: {wallet.get_events()}")
            print(f"Balance: {wallet.current_balance}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
