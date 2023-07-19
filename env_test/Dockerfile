FROM ubuntu:20

RUN apt-get -y update && apt-get install -y

RUN apt-get -y install clang

COPY . /usr/src/dockertest1

WORKDIR /usr/src/dockertest1

RUN clang++ -o env_test env_test.cpp

CMD [ "./env_test" ]