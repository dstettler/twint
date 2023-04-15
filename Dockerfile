FROM python:3.11-buster
LABEL maintainer="codyzacharias@pm.me"

WORKDIR /root

ADD . /root/twint

RUN cd /root/twint && \
	pip3 install -r requirements.txt && \
	pip3 install ./

CMD /bin/bash
