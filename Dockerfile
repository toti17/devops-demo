FROM python:3.8-alpine

Workdir /demo

COPY src/ .

CMD ["/bin/sh"]
