from bank import Bank

def main():
    bank = Bank()
    print(bank.register("Mohamed", "password123"))
    print(bank.register("Mohamed", "password123"))

    user1 = bank.login("Mohamed", "password123")
    user2 = bank.login("Salem", "password123")

    print('User1 Attempt')
    if isinstance(user1, str):
        print(user1)
    else:
        print(user1.deposit(1000))
        print(user1.check_balance())
        print(user1.withdraw(500))
    print('User2 Attempt')
    if isinstance(user2, str):
        print(user2)
    else:
        print(user2.deposit(1000))
        print(user2.check_balance())
        print(user2.withdraw(500))

if __name__ == "__main__":
    main()
