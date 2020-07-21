# makefile for linux
#
# Copyright 2016 Oyster

CC = gcc
CFLAGS = -g -Wall -O2
LDFLAGS =
INCLUDES = 
LIBS = -lstdc++

SRCS = $(wildcard *.cpp)
APPS = $(SRCS:%.cpp=bin/%)
OBJS = $(SRCS:%.cpp=obj/%.o)
DEPS = helper.h

all: mkdirs $(APPS)

$(APPS): bin/% : obj/%.o
	$(CC) $(LDFLAGS) $(LIBS) -o $@ $<

$(OBJS): obj/%.o : %.cpp $(DEPS)
	$(CC) $(CFLAGS) $(INCLUDES) -c -o $@ $<

mkdirs: bin obj

bin:
	mkdir -pv bin
obj:
	mkdir -pv obj

.PHONY: clean cleanall
clean:
	rm $(APPS) $(OBJS)

cleanall:
	rm -fr obj bin
