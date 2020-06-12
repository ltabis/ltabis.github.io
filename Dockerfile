FROM python:latest

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -r requirement.txt

CMD python app.py