import aiohttp_jinja2
from aiohttp_security import check_permission, authorized_userid


class VacancyRouter:

    async def index(self, request):
        pass

    async def create(self, request):
        pass

    @aiohttp_jinja2.template('pages/vacancy/vacancy_create.html')
    async def create_page(self, request):
        await check_permission(request, 'company')
        username = await authorized_userid(request)
        context = {
            'username': username,
            'title': 'Company page',
            'profile_link': 'company',
            'employer': False
        }
        return context

    async def one_page(self, request):
        pass

    def configure(self, app):
        router = app.router

        router.add_route('GET', '/vacancy/create', self.create_page, name='create_vacancy')
        router.add_route('POST', '/vacancy/create', self.create, name='create_vacancy')
