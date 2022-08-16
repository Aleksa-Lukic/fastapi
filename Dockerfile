FROM python:3.9


WORKDIR /fastapi

COPY ./requierements.txt /fastapi/requierements.txt
COPY ./app fastapi/app

RUN pip install --no-cache-dir -r requierements.txt


CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000" ]


