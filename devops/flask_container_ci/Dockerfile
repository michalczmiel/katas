FROM python:3.9.6-slim

RUN apt-get update && apt-get -y upgrade

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY users.json .

COPY app .

ENV FLASK_APP=app/main.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
