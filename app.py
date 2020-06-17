from flask import Flask, render_template
from sys import stderr
from backend.projects import create_project_templates

app = Flask(__name__)

@app.route('/')
def index():

    project_templates = create_project_templates()
    static = render_template('index.html', projects=project_templates)

    with open('./index.html', 'w') as file:
        file.write(static)

    return static

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)