FROM python:3.9.10-slim

RUN pip3 install flask

WORKDIR /portal
COPY app/ .

EXPOSE 5000

CMD [ "python3", "-u", "main.py" ]
