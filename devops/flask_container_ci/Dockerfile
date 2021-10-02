FROM python:3.9.6-slim

RUN apt-get update && apt-get -y upgrade

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY users.json .

COPY app app/

COPY scripts/entrypoint.sh .

# Run as non-root user
RUN useradd --create-home appuser
USER appuser

ENTRYPOINT [ "./entrypoint.sh" ]
