

class SpamSender:
    def __init__(self, session, sender):
        SpamSender.session = session
        SpamSender.sender = sender

    def send_emails(self, sender, subject, body):
        pass
