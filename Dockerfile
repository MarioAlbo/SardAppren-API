FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "/bin/sh",  "start.sh" ]
