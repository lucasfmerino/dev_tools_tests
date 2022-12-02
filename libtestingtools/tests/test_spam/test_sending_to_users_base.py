from libtestingtools.spam.main import SpamSender
from libtestingtools.spam.models import User
from unittest.mock import Mock
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
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'lucasfmerino@gmail.com',
        'Libtestingtools news #001',
        'Check out the fantastic modules!')
    assert len(users) == sender.send.call_count


def test_spam_parameters(session):
    user = User(name='Lucas', email='lucasfmerino@gmail.com')
    session.save_user(user)
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_emails(
        'lfmgames@gmail.com',
        'Libtestingtools news #001',
        'Check out the fantastic modules!')
    sender.send.assert_called_once_with(
        'lfmgames@gmail.com',
        'lucasfmerino@gmail.com',
        'Libtestingtools news #001',
        'Check out the fantastic modules!'
    )
