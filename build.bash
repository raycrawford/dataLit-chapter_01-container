#!/bin/bash

if [ -f ./Dockerfile ] && [ $1 == '-f' ]; then
  export docker_root=`pwd`
  if [ ! -f ./files/2600-0.txt ]; then
    mkdir files
    cd ./files
    echo "Downloading War and Peace"
    wget https://www.gutenberg.org/files/2600/2600-0.txt
    cd ${docker_root}
  fi
  docker build --tag data-lit .
  # Run the container; note that it gets destroyed every time so make sure any files exist in /root/files
  docker run --rm --name data-lit -it -v ${docker_root}/files:/root/files data-lit
else
  echo "You must be in the root of the newly cloned repo.  Change directory to the path where the Dockerfile exists."
fi
