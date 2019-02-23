# Purpose

This is a super simple Docker workflow for doing the work found in Chapter 1, "Data Collection" of the School of AI's class, "Data Lit".  I set this up because I didn't like the idea of relying on a web-based interface as suggested in the course content ([Google Co Labs](https://colab.research.google.com), at least initially...) and I don't like installing things on my local machine.

The workflow creates a container and mounts a directory `files` into the container at `/root/files`.  This was done so that I could use Visual Code on my Mac for editing while keeping all of the installed libraries and such inside the container (and off my Mac).

# Use

To use this workflow, clone the repo to your local file system.  Once there, replace the docker_root variable with the path that includes the Dockerfile found in this repo.

