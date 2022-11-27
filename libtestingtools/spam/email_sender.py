class Sender:
    def send(self, sender, addressee, subject, body):
        if '@' not in sender:
            raise InvalidMail(f'Invalid sender: {sender}')
        return sender

class InvalidMail(Exception):
    pass