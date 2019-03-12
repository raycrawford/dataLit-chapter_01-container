#!/bin/bash
IMAGE_EXISTS="$(docker images -q data-lit 2> /dev/null)"

if [ -f ./Dockerfile ]; then
  docker_root=`pwd`
  if [ ! -f ./files/2600-0.txt ]; then
    mkdir files
    cd ./files
    echo "Downloading War and Peace"
    wget https://www.gutenberg.org/files/2600/2600-0.txt
    cd ${docker_root}
  fi
  if [[ ! ${IMAGE_EXISTS} ]] || [[ $1 == '-f' ]]; then
    docker build --tag data-lit .
  fi
else
  echo "You must be in the directory with the Dockerfile."
  exit
fi

# Run the container; note that it gets destroyed every time so make sure any files exist in /root/files
docker run --rm --name data-lit -it -v ${docker_root}/files:/root/files data-lit
