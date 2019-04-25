FROM python:3.7-alpine
ADD . /course-work
WORKDIR /course-work
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev \
    && pip3 install -r requirements-dev.txt