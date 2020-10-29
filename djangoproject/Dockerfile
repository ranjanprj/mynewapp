FROM python:3.8-slim-buster
# RUN \
#  apk add --no-cache postgresql-libs && \
#  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
#  apk --purge del .build-deps


RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y netcat

RUN adduser python
USER python

ENV PYTHONUNBUFFERED 1
WORKDIR /home/python
COPY requirements.txt /home/python/


RUN pip install -r requirements.txt
COPY . /home/python/

COPY --chown=python:python requirements.txt .
ENV PATH="/home/python/.local/bin:${PATH}"
RUN pip install --user -r requirements.txt
COPY --chown=python:python src src

# RUN ["python", "src/project/manage.py", "makemigrations"]
# RUN ["python", "src/project/manage.py", "migrate"]
CMD ["python", "src/project/manage.py", "runserver", "0.0.0.0:8000"]

 
# ENTRYPOINT ["src/entrypoint.sh"]