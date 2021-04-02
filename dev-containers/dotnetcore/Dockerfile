FROM debian:latest
 
ARG USER=user

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN rm -rf /tmp/* /usr/share/doc/* /usr/share/info/* /var/tmp/*
RUN useradd -ms /bin/bash $USER
ENV DISPLAY :0

RUN apt-get install -y wget x11-utils
RUN wget https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb 
RUN dpkg -i packages-microsoft-prod.deb 
RUN apt-get update
RUN apt-get install -y dotnet-sdk-5.0

USER $USER
WORKDIR /home/$USER
ENTRYPOINT ["/bin/sh", "-c", "$0 \"$@\"", "/bin/bash"]
