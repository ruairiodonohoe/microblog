FROM python:slim

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY src/ .
COPY migrations migrations
COPY config.py boot.sh ./
RUN chmod a+x boot.sh

ENV PYTHONPATH=/src
ENV FLASK_APP=wsgi.py


EXPOSE 5000
ENTRYPOINT ["./boot.sh"]