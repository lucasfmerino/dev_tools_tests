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
    sender = Sender()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'lucasfmerino@gmail.com',
        'Libtestingtools news #001',
        'Check out the fantastic modules!')
    assert len(users) == sender.amount_of_emails_sent
