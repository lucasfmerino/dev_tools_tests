import requests
# pip install requests


def search_avatar(user):
    """
    Search a user's avatar from Github.
    Param: Github user name (str)
    Return: Github avatar link (str)
    """
    url = f"https://api.github.com/users/{user}"
    ans = requests.get(url)
    return ans.json()['avatar_url']
