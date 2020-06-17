from flask import render_template, Markup
from sys import stderr
from .github_api import connect_to_github 


def create_profile_template():
    """I could just hardcode with html.
       Why am I doing this.
       What is wrong with me.
    """

    auth = connect_to_github()

    name = auth.get_user().name
    pic = auth.get_user().avatar_url
    bio = auth.get_user().bio

    return Markup(render_template('profile.html', name=name, pic=pic, bio=bio))
