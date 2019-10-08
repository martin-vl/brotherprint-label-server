# Dockerfile
FROM python:2.7.10

COPY ./source /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]