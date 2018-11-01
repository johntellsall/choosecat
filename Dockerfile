FROM python:3.6

RUN apt-get update -y && \
    apt-get install -y vim && \
    pip install --upgrade pip setuptools

WORKDIR /app
CMD [ "python", "choosecat.py" ]

# We copy this file first to leverage docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip install -qr requirements.txt

# COPY . /app
