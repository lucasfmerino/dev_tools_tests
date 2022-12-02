from libtestingtools.spam.email_sender import Sender
from libtestingtools.spam.main import SpamSender
from libtestingtools.spam.models import User
import pytest


@pytest.mark.parametrize(
    'users', [
        [
            User(name='Lucas', email='lucasfmerino@gmail.com'),
            User(name='Arthur', email='lfmgames@gmail.com')
        ],
        [
            User(name='Lucas', email='lucasfmerino@gmail.com')
        ]
    ]
)
def test_spam_amount(session, users):
    for user in users:
        session.save_user(user)
    sender = SenderMock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'lucasfmerino@gmail.com',
        'Libtestingtools news #001',
        'Check out the fantastic modules!')
    assert len(users) == sender.amount_of_emails_sent


class SenderMock(Sender):
    def __init__(self):
        super().__init__()
        self.amount_of_emails_sent = 0
        self.shipping_parameters = None

    def send(self, sender, addressee, subject, body):
        self.shipping_parameters = (sender, addressee, subject, body)
        self.amount_of_emails_sent += 1


def test_spam_parameters(session):
    user = User(name='Lucas', email='lucasfmerino@gmail.com')
    session.save_user(user)
    sender = SenderMock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'lfmgames@gmail.com',
        'Libtestingtools news #001',
        'Check out the fantastic modules!')
    assert sender.shipping_parameters == (
        'lfmgames@gmail.com',
        'lucasfmerino@gmail.com',
        'Libtestingtools news #001',
        'Check out the fantastic modules!'
    )

