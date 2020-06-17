from github import Github
from flask import render_template, Markup
from sys import stderr
from os import getenv

def create_project_templates():
    """Create a template for each choosen project.

    Returns:
        Template[]: an array of html templates. 
    """

    auth = connect_to_github()

    projects = [
        "ltabis/electron-dev-environment",
        "matteovol/EclataxEngine",
        "ltabis/raytracer",
        "ltabis/Utility-scripts",
        "ltabis/MinecraftBackupTool",
        "ltabis/toDoJAVA",
    ]

    template_array = []

    for project in projects:

        repo = auth.get_repo(project)

        template_array.append(
            Markup(render_template('project_card.html', title=repo.name, link=repo.html_url, desc=repo.description))
        )

    return template_array


def connect_to_github():

    if not getenv('GITHUB_USER') or not getenv('GITHUB_PASSWORD'):
        raise EnvironmentError('GITHUB_USER & GITHUB_PASSWORD variables are missing.')

    return Github(getenv('GITHUB_USER'), getenv('GITHUB_PASSWORD'))