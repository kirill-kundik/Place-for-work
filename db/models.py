from datetime import datetime

from sqlalchemy import (
    MetaData, Table, Column, Integer, Float, Date,
    DateTime, Boolean, String, Text, ForeignKey
)

__all__ = ['company', 'category', 'status', 'phones', 'address', 'working_type', 'vacancy', 'response',
           'resume_experience', 'resume', 'employer', 'messages', 'news']

meta = MetaData()

status = Table(
    'status', meta,

    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
)

company = Table(
    'company', meta,

    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('email', String(255), nullable=False),
    Column('description', Text),
    Column('image_url', String(255)),
    Column('employers_cnt', Integer),
    Column('est_year', Integer),
    Column('site_url', String(4096)),
    Column('main_category', String(255), nullable=False),

    Column('status_fk', Integer, ForeignKey('status.id', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False),
)

phones = Table(
    'phones', meta,

    Column('id', Integer, primary_key=True),
    Column('phone', String(20), nullable=False),

    Column('company_fk', Integer, ForeignKey('company.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False),
)

address = Table(
    'address', meta,

    Column('id', Integer, primary_key=True),
    Column('city', String(200), nullable=False),
    Column('country', String(200), nullable=False),
    Column('street', String(300), nullable=False),
    Column('building', String(10), nullable=False),

    Column('company_fk', Integer, ForeignKey('company.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False),
)

category = Table(
    'category', meta,

    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('description', Text)
)

working_type = Table(
    'working_type', meta,

    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False)
)

vacancy = Table(
    'vacancy', meta,

    Column('id', Integer, primary_key=True),
    Column('position', String(100), nullable=False),
    Column('description', Text, nullable=False),
    Column('requirements', Text, nullable=False),
    Column('salary', Float),

    Column('working_type_fk', Integer, ForeignKey('working_type.id', ondelete='RESTRICT', onupdate='CASCADE'),
           nullable=False),
    Column('company_fk', Integer, ForeignKey('company.id', ondelete='CASCADE', onupdate='CASCADE'),
           nullable=False),
    Column('category_fk', Integer, ForeignKey('category.id', ondelete='RESTRICT', onupdate='CASCADE'),
           nullable=False)
)

employer = Table(
    'employer', meta,

    Column('id', Integer, primary_key=True),
    Column('first_name', String(200), nullable=False),
    Column('last_name', String(200), nullable=False),
    Column('email', String(255), nullable=False),
    Column('phone', String(20), nullable=False),

    Column('tg_link', String(200)),
    Column('fb_link', String(200)),
    Column('skype_link', String(200)),

    Column('city', String(200)),
    Column('date_of_birth', Date)
)

resume = Table(
    'resume', meta,

    Column('id', Integer, primary_key=True),
    Column('perks', Text, nullable=False),
    Column('hobbies', Text),

    Column('category_fk', Integer, ForeignKey('category.id', ondelete='RESTRICT', onupdate='CASCADE'),
           nullable=False),
    Column('employer_fk', Integer, ForeignKey('employer.id', ondelete='CASCADE', onupdate='CASCADE'),
           nullable=False)
)

resume_experience = Table(
    'resume_experience', meta,

    Column('id', Integer, primary_key=True),
    Column('title', String(100), nullable=False),
    Column('description', Text, nullable=False),
    Column('starting_date', Date, nullable=False),
    Column('ending_date', Date),

    Column('resume_fk', Integer, ForeignKey('resume.id', ondelete='CASCADE', onupdate='CASCADE'),
           nullable=False)
)

response = Table(
    'response', meta,

    Column('id', Integer, primary_key=True),
    Column('employer_fk', ForeignKey('employer.id', ondelete='CASCADE'), nullable=False),
    Column('company_fk', ForeignKey('company.id', ondelete='CASCADE'), nullable=False),

    Column('entry_msg', Text, nullable=False),
    Column('interview_date', DateTime)
)

messages = Table(
    'messages', meta,

    Column('id', Integer, primary_key=True),
    Column('date', DateTime, nullable=False, default=datetime.utcnow),
    Column('text', Text, nullable=False),
    Column('is_edited', Boolean, nullable=False, default=True),

    Column('to', Integer, ForeignKey('employer.id', ondelete='CASCADE', onupdate='CASCADE'),
           nullable=False),
    Column('from', Integer, ForeignKey('company.id', ondelete='CASCADE', onupdate='CASCADE'),
           nullable=False)
)

news = Table(
    'news', meta,

    Column('id', Integer, primary_key=True),
    Column('title', String(255), nullable=False),
    Column('text', Text, nullable=False),
    Column('date', Date, nullable=False, default=datetime.today),
    Column('views', Integer, nullable=False, default=0),

    Column('category_fk', Integer, ForeignKey('category.id', ondelete='RESTRICT', onupdate='CASCADE'),
           nullable=False)
)
