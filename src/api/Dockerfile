FROM python:latest

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . /api
WORKDIR /api
RUN python setup.py install
RUN rm -rf /api

COPY ./main.py /usr/local/cpu_loader/main.py
WORKDIR /usr/local/cpu_loader

ENV CACHE_TYPE simple
ENV SHORT_TIMEOUT 10
ENV MID_TIMEOUT 100
ENV LONG_TIMEOUT 1000
ENV WEB_PORT 80

CMD /usr/local/bin/gunicorn -w 4 -b :$WEB_PORT main:app