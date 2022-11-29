from libtestingtools.spam.email_sender import Sender
from libtestingtools.spam.main import SpamSender


def sending_spam(session):
    spam_sender = SpamSender(session, Sender())
    spam_sender.send_emails(
        'lucasfmerino@gmail.com',
        'Libtestingtools news #001',
        'Check out the fantastic modules!'
        )
