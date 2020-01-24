FROM ubuntu:18.04

RUN apt-get update && \ 
    apt-get install --no-install-recommends -y \ 
                    python3-pip \ 
                    python3-dev \
                    python3-setuptools \
                    iputils-ping \
                    telnet && \
    apt-get clean


WORKDIR /opt

ADD ./app /opt/app/
ADD ./glue-app /opt/glue-app/
ADD ./requirements.txt /opt/

RUN /usr/bin/python3 -m pip install -r /opt/requirements.txt

ENTRYPOINT [ "/bin/bash", "-c", "tail -f /dev/null" ] 