PLACE FOR WORK
==============

Course work that are being created by **Kundik Kyrylo**, Software Engineering 3rd year

*National University of Kyiv-Mohyla Academy*

This project using aiohttp_, aiopg_ and aiohttp_jinja2_, sqlalchemy_.


Requirements and steps to start app
-----------------------------------

First of all, you need a Python_ installed and Postgres_ or Docker_ by your decision.

Firstly, run Postgres DB server:

**Mac**::

    $ pg_ctl -D /usr/local/var/postgres start

or::

    $ brew services start postgresql

**Windows**::

    > pg_ctl -D "C:\Program Files\PostgreSQL\9.6\data" start

**In docker**::

    $ docker run --rm -it -p 5432:5432 postgres:10


Install all needed requirements with pip_::

    $ pip install -r requirements-dev.txt

On this step database will be created and some sample data will be inserted::

    $ python init_db.py


Run
---
Run application::

    $ python -m backend

Open browser::

    http://localhost:8081/



Requirements
============
* Python_
* pip_
* aiohttp_
* aiopg_
* aiohttp_jinja2_
* sqlalchemy_
* Docker_ or Postgres_



.. _Python: https://www.python.org
.. _aiohttp: https://github.com/aio-libs/aiohttp
.. _aiopg: https://github.com/aio-libs/aiopg
.. _aiohttp_jinja2: https://github.com/aio-libs/aiohttp_jinja2
.. _sqlalchemy: https://www.sqlalchemy.org
.. _Postgres: https://www.postgresql.org
.. _Docker: https://www.docker.com
.. _pip: https://pip.pypa.io/en/stable/installing/