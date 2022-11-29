
from libtestingtools.spam.models import User


def test_save_user(session):
    user = User(name='Lucas')
    session.save_user(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [User(name='Lucas'), User(name='Arthur')]
    for user in users:
        session.save_user(user)
    assert users == session.list_it()
