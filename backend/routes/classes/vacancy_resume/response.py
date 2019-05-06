from aiohttp import web
from aiohttp_security import check_permission, authorized_userid
from db import db


class ResponseRouter:
    # TODO
    async def response_status_update(self, request):
        pass

    # TODO
    async def vacancy_responses(self, request):
        pass

    # TODO
    async def delete_response(self, request):
        pass

    async def make_response(self, request):
        await check_permission(request, 'employer')
        username = await authorized_userid(request)
        form = await request.post()
        vacancy_fk = form.get('vac_id')
        async with request.app['db'].acquire() as conn:
            await db.make_response(conn, username, vacancy_fk)
        return web.HTTPFound(f'/vacancy/{vacancy_fk}')

    def configure(self, app):
        router = app.router

        router.add_route('POST', '/response/make', self.make_response, name='make_response')
        router.add_route('GET', '/response/{v_id}', self.vacancy_responses, name='vacancy_responses')
        router.add_route('POST', '/response/update', self.response_status_update, name='response_update')
        router.add_route('POST', '/response/delete', self.delete_response, name='delete_response')
