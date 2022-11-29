class Sender:
    def __init__(self):
        self.amount_of_emails_sent = 0

    def send(self, sender, addressee, subject, body):
        if '@' not in sender:
            raise InvalidMail(f'Invalid sender: {sender}')
        self.amount_of_emails_sent += 1
        return sender


class InvalidMail(Exception):
    pass
