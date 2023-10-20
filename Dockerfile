FROM python:3.11-slim-bullseye

WORKDIR /app

ENV PORT_APP=8080 \
  TZ=America/Sao_Paulo 

COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD gunicorn --workers $WORKERS \
  --threads $THREADS \
  --bind 0.0.0.0:$PORT_APP \
  app:app