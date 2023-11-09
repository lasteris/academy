FROM python:3.12.0-alpine3.18

RUN apk --no-cache add gcc musl-dev

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app

CMD ["academy.py"]
ENTRYPOINT [ "python3"]