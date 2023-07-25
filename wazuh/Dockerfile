FROM ubuntu:22.04

ENV APP_HOME "/app"

RUN echo 'root:root' | chpasswd

RUN apt-get -y update && \
    apt-get -y install build-essential && \
    apt install -y make && \
    rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_HOME}

COPY . ${APP_HOME}

ENTRYPOINT exec /bin/bash