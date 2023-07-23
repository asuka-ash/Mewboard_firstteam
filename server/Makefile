CC = g++

all: server

server: server.o
	${CC} -o server server.o

server.o: server.cpp
	$(CC) -c -g server.cpp
clean:
	rm server.o server