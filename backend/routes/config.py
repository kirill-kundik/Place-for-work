# routes.py
import pathlib

from backend.routes.classes.profiles.admin import AdminRouter
from backend.routes.classes.category import CategoryRouter
from backend.routes.classes.profiles.company import CompanyRouter
from backend.routes.classes.profiles.employer import EmployerRouter
from backend.routes.classes.index import IndexRouter
from backend.routes.classes.login import LoginRouter
from backend.routes.classes.news import NewsRouter
from backend.routes.classes.search import SearchRoute
from backend.routes.classes.vacancy_resume.resume import ResumeRouter
from backend.routes.classes.vacancy_resume.vacancy import VacancyRouter

PROJECT_ROOT = pathlib.Path(__file__).parent.parent


def setup_routes(app):
    setup_static_routes(app)

    routes = [AdminRouter, CategoryRouter, CompanyRouter, EmployerRouter, IndexRouter, LoginRouter, NewsRouter,
              VacancyRouter, SearchRoute, ResumeRouter]

    for route in routes:
        r = route()
        r.configure(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=PROJECT_ROOT / 'static',
                          name='static')
