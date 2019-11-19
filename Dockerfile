FROM ubuntu

RUN apt-get update
RUN apt-get -y install python python-pip vim
RUN pip install flask
RUN mkdir templates
COPY hello.html /templates
COPY app.py /opt


ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0

