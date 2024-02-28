## Technology Used
- Nginx and Gunicorn for Web Server.
- Docker for containerizing the application. Dockerfile and docker-compose to build image and container.
- API is made available in the form of json, created in Python.
- Makefile for running everything.
- Git for version control.

## Software Requirements
- Docker

## Instructions to Run
- To build image and start the containers:
    docker-compose up --build

- To stop the application and remove containers:
    docker-compose down

- TO start Jenkins:
    docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11

<!-- # resume-website
Run the commands to build and run the Docker image:
$ docker build -t httpd_1 .
$ docker run -dit --name my-running-app -p 80:80 httpd_1 -->

<!-- docker run -it --rm --cpus 4 --memory 3G -v  -->


<!-- docker-compose build --no-cache
docker-compose up -d 
docker-compose down -->


<!-- Build and run together:
docker-compose up --build -->