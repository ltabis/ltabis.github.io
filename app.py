from flask import Flask, render_template
from sys import stderr
from backend.projects import create_project_templates

app = Flask(__name__)

@app.route('/')
def index():

    project_templates = create_project_templates()

    with open('./index.static.html', 'w') as file:
        file.write(render_template('index.html', projects=project_templates))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)