FROM python:3.9

COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install -y vim less
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt