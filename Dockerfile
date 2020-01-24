FROM ubuntu:18.04

RUN apt-get update && \ 
    apt-get install --no-install-recommends -y \ 
                    python3-pip \ 
                    python3-dev \
                    python3-setuptools \
                    iputils-ping \
                    telnet && \
    apt-get clean

RUN /usr/bin/python3 -m pip install -U paho-mqtt pymongo

WORKDIR /opt

ADD ./app /opt/app/
ADD ./glue-app /opt/glue-app/

ENTRYPOINT [ "/bin/bash", "-c", "tail -f /dev/null" ] 