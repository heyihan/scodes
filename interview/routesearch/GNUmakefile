# makefile for linux
#
# Copyright 2016 Oyster

CC = gcc
CXX = g++
CFLAGS = -std=c++11 -I./src
LDFLAGS = 
LIBS = -lstdc++

TARGETS = bin/test
OBJS = obj/test.o obj/directedgraph.o obj/shortestpath.o

all: mkdirs $(TARGETS)

mkdirs: bin obj

bin:
	mkdir -pv bin
obj:
	mkdir -pv obj

bin/test: $(OBJS)
	$(CC) -o $@ $(LIBS) $(LDFLAGS) $^

obj/%.o:src/%.c
	$(CC) -c $(CFLAGS) -o $@ $<

obj/%.o:src/%.cpp
	$(CXX) -c $(CFLAGS) -o $@ $<

clean:
	rm $(TARGETS) $(OBJS)

cleanall:
	rm -fr obj bin
