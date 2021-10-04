FROM ubuntu:latest
RUN apt-get update
RUN apt-get install firefox -y
RUN apt-get install software-properties-common -y
RUN apt-get install less -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install python3.8 -y
RUN apt-get install python3-pip -y
RUN groupadd -g 1000 bmzi && useradd -d /home/bmzi -s /bin/bash -m bmzi -u 1000 -g 1000
USER bmzi
ENV HOME /home/bmzi


# Install pip requirements
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /home/bmzi/app
COPY . /home/bmzi/app

CMD ["python3", "bk.py"]
