FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /nutra

ADD . /nutra

COPY ./requirements.txt /nutra/requirements.txt

RUN pip install -r requirements.txt

COPY . /nutra

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]


