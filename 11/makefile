CC=g++
CFLAGS=-c -Wall -std=c++11
LDFLAGS=
SOURCES=d11-2.cc
OBJECTS=$(SOURCES:.cc=.o)
EXECUTABLE=foobar

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cc.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	$(RM) *.o
