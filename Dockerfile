FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    pip install --upgrade pip setuptools

WORKDIR /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

# We copy this file first to leverage docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip install -qr requirements.txt

COPY . /app
