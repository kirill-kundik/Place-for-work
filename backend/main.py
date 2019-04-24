import logging
import sys

import aiohttp_jinja2
import jinja2
from aiohttp import web

from backend.elastic import init_es, close_es
from backend.security.init_security import init_security
from db.db import close_pg, init_pg
from backend.routes.middlewares import setup_middlewares
from backend.routes.config import setup_routes
from backend.settings import get_config


async def init_app(argv=None):
    app = web.Application()

    print('...Reading configs...')
    app['config'] = get_config(argv)

    # setup Jinja2 template renderer
    print('...Set up jinja2...')
    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('backend', 'templates'))

    # create db connection on startup, shutdown on exit
    print('...Appending startup tasks...')
    app.on_startup.append(init_pg)
    app.on_startup.append(init_security)
    app.on_cleanup.append(close_pg)
    print('...Set up ElasticSearch...')
    app.on_startup.append(init_es)
    app.on_cleanup.append(close_es)

    # setup views and routes
    print('...Set up routes...')
    setup_routes(app)
    print('...Set up middlewares...')
    setup_middlewares(app)

    return app


def main(argv):
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(argv)

    config = get_config(argv)
    print('...Starting app...')
    web.run_app(app,
                host=config['host'],
                port=config['port'])


if __name__ == '__main__':
    main(sys.argv[1:])
