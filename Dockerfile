FROM python:3.7

# RUN apt-get update && \ 
#     apt-get install --no-install-recommends -y \ 
#                     python3-pip \ 
#                     python3-dev \
#                     python3-setuptools \
#                     iputils-ping \
#                     telnet && \
#     apt-get clean


WORKDIR /opt

ADD ./app /opt/app/
ADD ./glue-app /opt/glue-app/
ADD ./requirements.txt /opt/

RUN /usr/local/bin/python -m pip install -r /opt/requirements.txt

ENTRYPOINT [ "/usr/local/bin/python", "/opt/glue-app/mqtt.py" ] 
