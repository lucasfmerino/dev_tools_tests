from time import sleep


class Session:
    counter = 0
    users = []

    def save_user(self, user):
        Session.counter += 1
        user.id = Session.counter
        self.users.append(user)

    def list_it(self):
        return self.users

    def roll_back(self):
        self.users.clear()

    def close(self):
        pass


class Connection:
    def __init__(self):
        sleep(1)

    def generate_session(self):
        return Session()

    def close(self):
        pass
