from aiohttp_security import SessionIdentityPolicy
from aiohttp_security import setup as setup_security
from aiohttp_session import setup as setup_session
from aiohttp_session.redis_storage import RedisStorage
from aioredis import create_pool

from backend.security.db_auth import DBAuthorizationPolicy


async def init_security(app):
    redis_pool = await create_pool((app['config']['redis']['host'], app['config']['redis']['port']))

    setup_session(app, RedisStorage(redis_pool))
    setup_security(app,
                   SessionIdentityPolicy(),
                   DBAuthorizationPolicy(app['db']))
