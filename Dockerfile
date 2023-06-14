FROM python:3.9-alpine

EXPOSE 5000

ENV FLASK_APP=flaskr
ENV FLASK_DEBUG=1

COPY . /app

WORKDIR /app

RUN pip install --editable .

CMD [ "flask", "run", "--host=0.0.0.0" ]