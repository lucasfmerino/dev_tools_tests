from libtestingtools import api_github
from unittest.mock import Mock
import pytest


@pytest.fixture
def avatar_url(mocker):
    ans_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/116420402?v=4'
    ans_mock.json.return_value = {
        "login": "lucasfmerino",
        "id": 116420402,
        "node_id": "U_kgDOBvBvMg",
        "avatar_url": url,
    }
    get_mock = mocker.patch('libtestingtools.api_github.requests.get')
    get_mock.return_value = ans_mock
    return url


def test_search_avatar(avatar_url):
    url = api_github.search_avatar("lucasfmerino")
    assert avatar_url == url


def test_search_avatar_integration():
    url = api_github.search_avatar("lucasfmerino")
    assert 'https://avatars.githubusercontent.com/u/116420402?v=4' == url
