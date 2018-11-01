import os
import random

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def choose_cat():
    IMAGES = [
        "https://vignette.wikia.nocookie.net/randycunningham9thgradeninja/images/9/97/YES_cat.jpg/revision/latest",
        "https://i.imgur.com/DKUR9Tk.png",
    ]
    return random.choice(IMAGES)


def hello_world(request):
    cat = choose_cat()
    return Response(f'Hello World! 725<hr><img src="{cat}">')


if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("hello", "/")
        config.add_view(hello_world, route_name="hello")
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", int(os.environ["CHOOSECAT_PORT"]), app)
    server.serve_forever()
