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

    repository = auth.get_repo(repository)
    project_languages = repository.get_languages()
    code_badges = []

    for project_language in project_languages:
        badge_color = ''
        if "color" not in languages[project_language] or languages[project_language]["color"] is None:
            badge_color = '#111111'
        else:
            badge_color = languages[project_language]["color"]
        language_text_color = '#ffffff' if is_dark(badge_color[1:]) else '#111111'
        code_badges.append((project_language, language_text_color, badge_color))

    major_language_color = '#ffffff' if len(project_languages) == 0 else languages[repository.language]["color"]
    return Markup(render_template('project_card.html',
        badges=code_badges,
        title=repository.name,
        link=repository.html_url,
        desc=repository.description,
        image=asset,
        color=major_language_color,
        language_name=repository.language,
        language_url=repository.languages_url,
        language_text_color=language_text_color,
    ))


def is_dark(color):
    l = 0.2126 * int(color[0:2], 16) + 0.7152 * int(color[2:4], 16) + 0.0722 * int(color[4:6], 16)
    return False if l / 255 > 0.65 else True
