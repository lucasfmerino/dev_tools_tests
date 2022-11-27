import pytest
from libtestingtools.spam.email_sender import Sender, InvalidMail


def test_create_email_sender():
    sender = Sender()
    assert sender is not None


@pytest.mark.parametrize('senders', ["lucasfmerino@gmail.com", "lfmgames@gamil.com"])
def test_sender(senders):
    sender = Sender()
    result = sender.send(
        senders,  # Sender
        "oozzcoder@gmail.com",  # Addressee
        "Libtestingtools",  # Subject
        "First class open"  # Body
        )
    assert senders in result


@pytest.mark.parametrize('senders', ["", "lucas"])
def test_invalis_sender(senders):
    sender = Sender()
    with pytest.raises(InvalidMail):
        sender.send(
            senders,  # Sender
            "oozzcoder@gmail.com",  # Addressee
            "Libtestingtools",  # Subject
            "First class open"  # Body
            )
