FROM python:3.9-alpine as backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 'True'


WORKDIR /code

COPY base.txt /code/

RUN pip install --upgrade pip 

RUN apk --no-cache add \
        --virtual .requirements-build-deps \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev \
        zlib-dev \
        jpeg-dev \
        mariadb-connector-c-dev && \ 
    python3 -m pip install -r base.txt --no-cache-dir 





COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]