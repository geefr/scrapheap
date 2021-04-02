#!/usr/bin/env bash
APP=arduino
RUNFLAGS="--privileged"

docker build --build-arg USER=${USER} -t ${APP}-env .
docker run \
    -dit \
    --rm \
    --name ${APP} \
    --net=host \
    ${RUNFLAGS} \
    -e DISPLAY \
    -v ${HOME}/.Xauthority:/home/${USER}/.Xauthority \
    ${APP}-env \
    "$@"


