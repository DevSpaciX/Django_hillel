FROM python:3.10.8
ENV PYTHONUNBUFFERED = 1

RUN mkdir /mysite
WORKDIR mysite

COPY . .

RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000