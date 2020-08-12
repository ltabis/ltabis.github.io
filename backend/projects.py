from flask import render_template, Markup
from sys import stderr
import requests
import yaml

from .github_api import connect_to_github 

def create_project_templates():
    """Create a template for each choosen project.

    Returns:
        Template[]: an array of html templates. 
    """

    auth = connect_to_github()
    languages = get_github_language_colors()

    projects = {
        "ltabis/accounts-cli": "assets/dollar-logo.png",
        "ltabis/electron-dev-environment": "assets/electron-logo.png",
        "matteovol/EclataxEngine": "assets/cpp-logo.png",
        "ltabis/Utility-scripts": "assets/py-logo.png",
        "ltabis/raytracer": "assets/rust-logo.png",
        "ltabis/MinecraftBackupTool": "assets/mc-logo.png",
    }

    template_array = []

    for (project, image) in projects.items():

        repo = auth.get_repo(project)
        color = ''
        if languages[repo.language]["color"] is None:
            color = '#111111'
        else:
            color = languages[repo.language]["color"]
        language_text_color = '#ffffff' if is_dark(color[1:]) else '#111111'

        template_array.append(
            Markup(render_template('project_card.html',
                title=repo.name,
                link=repo.html_url,
                desc=repo.description,
                image=image,
                color=color,
                language_name=repo.language,
                language_url=repo.languages_url,
                language_text_color=language_text_color,
            ))
        )

    return template_array

def is_dark(color):
    l = 0.2126 * int(color[0:2], 16) + 0.7152 * int(color[2:4], 16) + 0.0722 * int(color[4:6], 16)
    return False if l / 255 > 0.65 else True

def get_github_language_colors():
    yaml_file = requests.get("https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml").text
    return yaml.safe_load(yaml_file)
