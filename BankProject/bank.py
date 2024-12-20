from user import User

class Bank:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            return 'Username already exists'
        self.users[username] = User(username, password)
        return 'User registered successfully'

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return 'Invalid username or password'

    def deposit(self, username, amount):
        user = self.users.get(username)
        if user:
            return user.deposit(amount)
        return 'User not found'

    def withdraw(self, username, amount):
        user = self.users.get(username)
        if user:
            return user.withdraw(amount)
        return 'User not found'
