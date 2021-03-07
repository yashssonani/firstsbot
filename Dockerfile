FROM python:3.8.5-slim-buster

WORKDIR /app

ENV PIP_NO_CACHE_DIR 1


RUN apt -qq update


COPY . .



RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "firstprobot"]
