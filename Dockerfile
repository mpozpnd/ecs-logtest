FROM python:latest

RUN pip install luigi
RUN pip install gokart

COPY ./conf /app/conf
COPY ./logtest /app/logtest
COPY ./main.py /app/main.py
COPY ./luigi.cfg /app/luigi.cfg



WORKDIR /app
VOLUME /app
