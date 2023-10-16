FROM python:3.11.4

RUN mkdir /sob

WORKDIR /sob

COPY req.txt .

RUN pip install -r req.txt

Copy . .

CMD gunicorn main:app --workers=2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000