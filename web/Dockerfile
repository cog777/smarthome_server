FROM debian:latest
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev python3-setuptools build-essential
RUN apt-get update
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["server.py"]
