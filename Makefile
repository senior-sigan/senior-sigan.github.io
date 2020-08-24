NAME ?= 'test_post'

post:
	hugo new --kind posts posts/$(NAME)

build:
	hugo

server:
	hugo server

clean:
	rm -rf public