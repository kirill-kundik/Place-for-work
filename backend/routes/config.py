# routes.py
import pathlib

from backend.routes.classes.profiles.admin import AdminRouter
from backend.routes.classes.category import CategoryRouter
from backend.routes.classes.profiles.company import CompanyRouter
from backend.routes.classes.profiles.employer import EmployerRouter
from backend.routes.classes.index import IndexRouter
from backend.routes.classes.login import LoginRouter
from backend.routes.classes.news import NewsRouter

PROJECT_ROOT = pathlib.Path(__file__).parent.parent


def setup_routes(app):
    # app.router.add_get('/poll/{question_id}', poll, name='poll')
    # app.router.add_get('/poll/{question_id}/results',
    #                    results, name='results')
    # app.router.add_post('/poll/{question_id}/vote', vote, name='vote')
    setup_static_routes(app)

    routes = [AdminRouter, CategoryRouter, CompanyRouter, EmployerRouter, IndexRouter, LoginRouter, NewsRouter]

    for route in routes:
        r = route()
        r.configure(app)
    #
    # index_routes = IndexRouter()
    # index_routes.configure(app)
    #
    # login_routes = LoginRouter()
    # login_routes.configure(app)
    #
    # admin_routes = AdminRouter()
    # admin_routes.configure(app)
    #
    # employer_routes = EmployerRouter()
    # employer_routes.configure(app)
    #
    # company_routes = CompanyRouter()
    # company_routes.configure(app)
    #
    # news_routes = NewsRouter()
    # news_routes.configure(app)
    #
    # category_routes = CategoryRouter()
    # category_routes.configure(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=PROJECT_ROOT / 'static',
                          name='static')
