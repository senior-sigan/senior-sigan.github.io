all: clean build

.PHONY:build
build:
	ssg

.PHONY:server
server:
	http-server build/

.PHONY:clean
clean:
	rm -rf build
