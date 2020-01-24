FROM ubuntu:18.04

RUN apt-get update && \ 
    apt-get install --no-install-recommends -y python3-pip python3-dev iputils-ping
    
CMD ["/bin/bash"] 