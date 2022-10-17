FROM python:3.10-slim

RUN pip3 install flask waitress

WORKDIR /portal
COPY app/ .

EXPOSE 5000

CMD [ "python3", "-u", "main.py" ]
