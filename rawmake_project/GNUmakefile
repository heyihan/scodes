# makefile for linux
#
# Copyright 2016 Oyster

CC = gcc
CFLAGS = 

TARGETS = bin/main
OBJS = obj/main.o

all: mkdirs $(TARGETS)

mkdirs: bin obj

bin:
	mkdir -pv bin
obj:
	mkdir -pv obj

bin/main: obj/main.o
	$(CC) -o $@ $<

obj/%.o:src/%.c
	$(CC) -c $(CFLAGS) -o $@ $<

clean:
	rm $(TARGETS) $(OBJS)

cleanall:
	rm -fr obj bin
