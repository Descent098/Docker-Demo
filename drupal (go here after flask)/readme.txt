This folder contains a docker-compose file. This is similar to a dockerfile but uses a different system.
Docker-compose is an orchestration tool (docker version of kubernetes), this means it will setup multiple images and containers at once.
Essentially this will setup a drupal 9 container, a DB container and it connects them together so they can speak to each other.
This is typically called a pod or swarm depending on your system 

To get this to work you need to run
    docker compose up

From there here is the drupal usage:

Head to http://localhost

You can login at http://localhost/user using
    Username: user
    password: bitnami


To take down the pod you cna use
    docker compose down
