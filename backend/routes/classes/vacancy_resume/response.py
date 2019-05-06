from aiohttp import web
from aiohttp_security import check_permission, authorized_userid
from db import db
import aiohttp_jinja2


class ResponseRouter:
    # TODO
    async def response_status_update(self, request):
        pass

    @aiohttp_jinja2.template('pages/responses/company_responses.html')
    async def vacancy_responses(self, request):
        await check_permission(request, 'company')
        username = await authorized_userid(request)
        v_id = request.match_info['v_id']
        async with request.app['db'].acquire() as conn:
            if not await db.check_company_vacancy(conn, username, v_id):
                raise web.HTTPUnauthorized
            vacancy = await db.get_vacancy(conn, v_id)

            statuses = []
            res = await db.get_vacancy_responses(conn, v_id)

            for s in res:
                statuses.append({
                    'id': s[0],
                    'resume_fk': s[1],
                    'status': s[3],
                    'entry_msg': s[4],
                    'interview_date': (s[5] if not s[5] else s[5].replace(microsecond=0).replace(second=0))
                })

            context = {
                'username': username,
                'title': 'Responses page',
                'profile_link': 'company',
                'employer': False,
                'vacancy_name': vacancy['position'],
                'vacancy_id': v_id,
                'statuses': statuses
            }

            return context

    async def delete_response(self, request):
        await check_permission(request, 'employer')
        username = await authorized_userid(request)
        form = await request.post()
        response_id = form.get('r_id')
        async with request.app['db'].acquire() as conn:
            await db.delete_response(conn, username, response_id)
        return web.HTTPFound('/employer')

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
