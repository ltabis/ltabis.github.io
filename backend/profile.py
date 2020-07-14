from flask import render_template, Markup
from sys import stderr
from .github_api import connect_to_github 
import toml

def create_profile_template():
    """I could just hardcode with html.
       Why am I doing this.
       What is wrong with me.
    """

    auth = connect_to_github()
    (version, date) = get_website_version()

    name = auth.get_user().name
    pic = auth.get_user().avatar_url
    bio = auth.get_user().bio

    location = auth.get_user().location
    email = auth.get_user().email
    company = auth.get_user().company

    return Markup(render_template('profile.html',
                                  name=name,
                                  pic=pic,
                                  bio=bio,
                                  email=email,
                                  location=location,
                                  company=company,
                                  version=version,
                                  date=date))

def get_website_version():

   parsed_toml = toml.load('project.toml')
   return parsed_toml['version']['number'], parsed_toml['version']['date']
