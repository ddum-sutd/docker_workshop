FROM python:3.9-slim

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir Flask

EXPOSE 5000

CMD ["python", "app.py"]
