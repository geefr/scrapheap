#!/usr/bin/env bash
APP=dotnetcore

if [ $# -ne 1 ]; then
  echo "USAGE: ./start.sh work-directory"
  exit 1
fi

WORKDIR=$1
RUNFLAGS="-v ${WORKDIR}:${WORKDIR}"

thisdir=$(dirname "${BASH_SOURCE[0]}")

cd ${thisdir}
docker build --build-arg USER=${USER} -t ${APP}-env .
docker run \
    -it \
    --rm \
    --name ${APP} \
    --net=host \
    -e DISPLAY \
    ${RUNFLAGS} \
    -v ${HOME}/.Xauthority:/home/${USER}/.Xauthority \
    ${APP}-env

