from flask import render_template, Markup
from sys import stderr
from .github_api import connect_to_github 

def create_project_templates():
    """Create a template for each choosen project.

    Returns:
        Template[]: an array of html templates. 
    """

    auth = connect_to_github()

    projects = {
        "ltabis/accounts-cli": "assets/dollar-logo.png",
        "ltabis/electron-dev-environment": "assets/electron-logo.png",
        "matteovol/EclataxEngine": "assets/cpp-logo.png",
        "ltabis/raytracer": "assets/rust-logo.png",
        "ltabis/toDoJAVA": "assets/java-logo.png",
        "ltabis/Utility-scripts": "assets/py-logo.png",
        "ltabis/MinecraftBackupTool": "assets/mc-logo.png",
    }

    template_array = []

    for (project, image) in projects.items():

        repo = auth.get_repo(project)

        template_array.append(
            Markup(render_template('project_card.html', title=repo.name, link=repo.html_url, desc=repo.description, image=image))
        )

    return template_array