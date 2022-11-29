
from libtestingtools.spam.models import User


def test_save_user(session):
    user = User(name='Lucas', email='lucasfmerino@gmail.com')
    session.save_user(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [User(name='Lucas', email='lucasfmerino@gmail.com'), User(name='Arthur', email='lfmgames@gmail.com')]
    for user in users:
        session.save_user(user)
    assert users == session.list_it()
