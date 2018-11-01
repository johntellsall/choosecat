import logging
import os
import random

import sqlalchemy
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from sqlalchemy.sql import text


def choose_cat():
    IMAGES = [
        "https://vignette.wikia.nocookie.net/randycunningham9thgradeninja/images/9/97/YES_cat.jpg/revision/latest",
        "https://i.imgur.com/DKUR9Tk.png",
    ]
    return random.choice(IMAGES)

def check_database():
    postgres_url = 'postgresql://postgres:{POSTGRES_PASSWORD}@db/database'.format(**os.environ)
    engine = sqlalchemy.create_engine(postgres_url)
    with engine.connect() as con:
        return con.execute('SELECT version()')

def hello_world(request):
    cat = choose_cat()
    return Response(f'Hello World! 725<hr><img src="{cat}">')


if __name__ == "__main__":
    logging.info('database: %s', check_database())
    with Configurator() as config:
        config.add_route("hello", "/")
        config.add_view(hello_world, route_name="hello")
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", int(os.environ["CHOOSECAT_PORT"]), app)
    server.serve_forever()
