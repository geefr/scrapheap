#!/usr/bin/env bash

cmake -DCMAKE_BUILD_TYPE=debug $(dirname "$0")

while true; do
  clear
  echo "---------------------------"
  cmake --build .
  if [ $? -ne 0 ]; then
    sleep 5
    continue
  fi
  
  echo "---------------------------"
 
  if [ "$(uname)" == "Darwin" ]; then
    ./proto $#
  elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    ./proto $#
  elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    ./Debug/proto.exe $#
  elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    ./Debug/proto.exe $#
  fi

  sleep 2
done

