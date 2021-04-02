FROM debian:latest
 
ARG USER=user

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN rm -rf /tmp/* /usr/share/doc/* /usr/share/info/* /var/tmp/*
RUN useradd -ms /bin/bash $USER
ENV DISPLAY :0

RUN apt-get install -y arduino
RUN usermod -aG dialout $USER

USER $USER
ENTRYPOINT ["/bin/sh", "-c", "$0 \"$@\"", "arduino"]
