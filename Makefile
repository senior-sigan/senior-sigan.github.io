all: clean build

.PHONY:build
build:
	poetry run python main.py

.PHONY:server
server:
	http-server build/

.PHONY:clean
clean:
	rm -rf build
