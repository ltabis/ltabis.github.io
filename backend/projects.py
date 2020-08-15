from flask import render_template, Markup
from sys import stderr
import requests
import yaml

from .github_api import connect_to_github 

def get_github_language_colors():
    yaml_file = requests.get("https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml").text
    return yaml.safe_load(yaml_file)

auth = connect_to_github()
languages = get_github_language_colors()

def create_project_templates():
    """Create a template for each choosen project.

    Returns:
        Template[]: an array of html templates. 
    """

    projects = {
        "ltabis/accounts-cli": "assets/dollar-logo.png",
        "matteovol/EclataxEngine": "assets/pad-logo.png",
        "ltabis/deBruijnSequence": "assets/haskell-logo.png",
        "ltabis/raytracer": "assets/rust-logo.png",
        "ltabis/GuessTheNumberQT": "assets/cpp-logo.png",
        "ltabis/lingo": "assets/c-logo.png",
        "ltabis/electron-dev-environment": "assets/electron-logo.png",
    }

    others = {
        "ltabis/Utility-scripts": "assets/py-logo.png",
        "ltabis/MyLibC": "assets/c-logo.png",
    }

    projects_array = []
    others_array = []

    for (project, image) in projects.items():
        project_template = create_project_html_template(project, image)
        projects_array.append(project_template)

    for (project, image) in others.items():
        project_template = create_project_html_template(project, image)
        others_array.append(project_template)

    return projects_array, others_array

def create_project_html_template(repository, asset):

    repo = auth.get_repo(repository)
    color = ''
    if languages[repo.language]["color"] is None:
        color = '#111111'
    else:
        color = languages[repo.language]["color"]
    language_text_color = '#ffffff' if is_dark(color[1:]) else '#111111'

    return Markup(render_template('project_card.html',
        title=repo.name,
        link=repo.html_url,
        desc=repo.description,
        image=asset,
        color=color,
        language_name=repo.language,
        language_url=repo.languages_url,
        language_text_color=language_text_color,
    ))


def is_dark(color):
    l = 0.2126 * int(color[0:2], 16) + 0.7152 * int(color[2:4], 16) + 0.0722 * int(color[4:6], 16)
    return False if l / 255 > 0.65 else True
