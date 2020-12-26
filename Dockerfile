FROM python:3.8.6

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app

CMD ["academy.py"]
ENTRYPOINT [ "python3"]