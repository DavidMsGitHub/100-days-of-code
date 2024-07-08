class User:
    def __init__(self, seats, username):
        self.seats = seats
        self.username = username

user1 = User(5, "Davita")

print(user1.username)