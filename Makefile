NAME ?= 'test_post'
YARN = node_modules/yarn/bin/yarn
HUGO = hugo

post:
	$(HUGO) new --kind posts posts/$(NAME)

build:
	cd themes/terminal && $(YARN) build
	$(HUGO)

server:
	$(HUGO) server

clean:
	rm -rf public

install:
	cd themes/terminal && \
	npm i && \
	npm i yarn && \
	$(YARN)