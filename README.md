# Docker-Demo
This repository is used to help teach about how docker works with a minimal example.

Start with the Flask demo and then move on to the drupal one.


## Network diagram

This diagram explains the basics of how a docker network talks to the outside world.

Following a network request and response:

1. First the client requests a URL (like kieranwood.ca)
2. The reverse proxy determines which host you need to talk to based on the request and forwards the request to it
3. The Host then talks to the containers to generate a response
4. The response is propogated from the container to the host machine, then to the reverse proxy and back to the client

<img src ="https://raw.githubusercontent.com/Descent098/Docker-Demo/main/network-diagram.svg">
