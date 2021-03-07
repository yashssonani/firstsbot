FROM python:3.8.5-slim-buster

WORKDIR /app

ENV PIP_NO_CACHE_DIR 1

RUN apt -qq install -y --no-install-recommends \
    git https://github.com/sahilpatel12345/firstprobot.git \  
    software-properties-common && \
    rm -rf /var/lib/apt/lists/* && \
    apt-add-repository non-free

RUN apt -qq update


COPY . .



RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "firstprobot"]
