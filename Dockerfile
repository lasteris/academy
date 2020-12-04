FROM python:3.8.6

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["academy.py"]
ENTRYPOINT [ "python3"]