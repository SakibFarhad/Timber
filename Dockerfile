FROM python:3.7

WORKDIR /opt

ADD ./app /opt/app/
ADD ./glue-app /opt/glue-app/
ADD ./requirements.txt /opt/

RUN /usr/local/bin/python -m pip install -r /opt/requirements.txt

ENTRYPOINT [ "/usr/local/bin/python", "/opt/glue-app/main.py" ] 
