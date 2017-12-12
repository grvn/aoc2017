CC=javac
CFLAGS=-g
LDFLAGS=
.SUFFIXES: .java .class
SOURCES=d121.java
OBJECTS=$(SOURCES:.java=.class)
EXECUTABLE=code

all: $(OBJECTS)

.java.class:
	$(CC) $(CFLAGS) $*.java

clean:
	$(RM) *.class
