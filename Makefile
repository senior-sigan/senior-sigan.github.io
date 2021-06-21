NAME ?= 'test_post'
YARN = node_modules/yarn/bin/yarn
HUGO = hugo

all: build

post:
	$(HUGO) new --kind posts posts/$(NAME)

build:
	$(HUGO)

server:
	$(HUGO) server

clean:
	rm -rf public
