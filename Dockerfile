FROM python:3.8.5-slim-buster

WORKDIR /app

RUN apt -qq update

COPY . .

RUN pip3 install https://github.com/sahilpatel12345/firstprobot/archive/main.zip

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "firstprobot"]
