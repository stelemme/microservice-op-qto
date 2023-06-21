FROM python:3.9-alpine

ENV FLASK_APP=flaskr

COPY . /app

WORKDIR /app

RUN pip install --editable .

CMD [ "flask", "run", "--host=0.0.0.0", "--port=80"]