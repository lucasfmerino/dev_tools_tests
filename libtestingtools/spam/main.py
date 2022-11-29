

class SpamSender:
    def __init__(self, session, sender):
        SpamSender.session = session
        SpamSender.sender = sender

    def send_emails(self, sender, subject, body):
        for user in self.session.list_it():
            self.sender.send(
                sender,
                user.email,
                subject,
                body
            )
