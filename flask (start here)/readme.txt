Steps locally to run the project
================================

1. Have a python 3 install with pip for python 3
2. install the requirements by running: pip install -r requirements.txt
3. Run the project by running: python routes.py
4. Head to your browser and visit http://localhost:8080


Using docker
============

1. Run `docker build -t flask-test .` This will create a docker container called flask-test
2. Run container using `docker run -dp 8080:8080 flask-test`, this runs the container and maps port 8080 of the host to the containers 8080 port
3. Go to http://localhost:8080 after finished building to see the app

To stop a docker container we will need the process ID. We currently have the image name (flask-test) so we can get the process id using:

    docker ps -a -q  --filter ancestor=flask-test

From there copy the ID it gives you and run: docker stop <id>

To clean up the image if you no longer want it you can use: docker image rm -f flask-test

Note that if you do this you will need to come into this folder again and run:
    docker build -t flask-test .
to be able to run using this config


Troubleshooting
===============
Most errors tend to occur because docker is not running. On windows open the docker desktop app 


Docker concepts & background info
=================================
Docker runs it's containers based off images. Images are generated using dockerfiles and the build command. 
Once an image is generated and built it can be used with:
    docker run

and a set of flags in order to configure your container


Docker networking
=================
- https://docs.docker.com/network/

(check out network-diagram.svg for a visual explanation)

You should know about IP addresses and ports before diving into docker. 
Essentially an IP address tells you where a computer (or container) is.
This is essential when you want to send network data between the host and the container.
Additionally multiple services can run on one device/container, therefore we need a way to specify where to look.
To do this we can use a port along with an IP to say exactly where we should go to get the data we need.
This would look something like this typically:
    127.0.0.1:8080
Where 127.0.0.1 is the IP address and 8080 is the port.
This means to access it with something like a browser the browser will go to computer 127.0.0.1 and ask for info at port 8080

Docker storage
==============
-  https://docs.docker.com/storage/
