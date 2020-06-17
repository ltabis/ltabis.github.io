
from github import Github
from os import getenv

def connect_to_github():

    if not getenv('GITHUB_USER') or not getenv('GITHUB_PASSWORD'):
        raise EnvironmentError('GITHUB_USER & GITHUB_PASSWORD variables are missing.')

    return Github(getenv('GITHUB_USER'), getenv('GITHUB_PASSWORD'))