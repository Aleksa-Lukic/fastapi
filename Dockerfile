FROM python:3.9


WORKDIR /fastapi

COPY ./requierements.txt /fastapi/requierements.txt
COPY ./app fastapi/app

RUN pip install --no-cache-dir -r requierements.txt


CMD [ "uvicorn", "app.main:app", "--host", "172.17.0.1", "--port", "5000" ]


