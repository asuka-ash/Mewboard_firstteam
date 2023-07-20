CC = g++

all: env_test

env_test: env_test.o
	${CC} -o env_test env_test.o -latomic

env_test.o: env_test.cpp
	$(CC) -c -g env_test.cpp
clean:
	rm env_test.o env_test