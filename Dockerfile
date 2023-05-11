FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /Blog

COPY requirements.txt requirements.txt
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 80


CMD ["uvicorn","main:app","--host","0.0.0.0 ","--port","80  ","--reload"]
