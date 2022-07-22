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


To take down the pod you can use
    docker compose down




I would also recommend installing some modules by going to the extend menu. 
From there you can add a new module and provide links to install them

Admin toolbar: https://www.drupal.org/project/admin_toolbar/releases/8.x-2.x-dev
Path Auto: https://ftp.drupal.org/files/projects/pathauto-8.x-1.x-dev.tar.gz
Token (required for Path Auto): https://ftp.drupal.org/files/projects/token-8.x-1.10.tar.gz
Webforms: https://ftp.drupal.org/files/projects/webform-6.1.x-dev.tar.gz
IMCE: https://ftp.drupal.org/files/projects/imce-8.x-2.4.tar.gz
Menu Block: https://ftp.drupal.org/files/projects/menu_block-8.x-1.8.tar.gz
Linkit: https://ftp.drupal.org/files/projects/linkit-8.x-5.0-beta13.tar.gz
