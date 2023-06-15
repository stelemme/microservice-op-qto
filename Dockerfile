FROM python:3.9-alpine

ENV PORT=3000
ENV FLASK_APP=flaskr
ENV FLASK_DEBUG=1

COPY . /app

WORKDIR /app

RUN pip install --editable .

EXPOSE 3000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=80"]