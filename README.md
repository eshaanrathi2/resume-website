## About
Objective of this project is to create a mock API (with dummy resume content) and perform validations on the API. Focus is on to orchestrate the following technologies.
<!-- Instructions to Run to get started with in on your machine. -->

## Technologies Used
- Nginx and Gunicorn for Web Server.
- Mock API with resume content is made available in the form of json.
- Docker for containerizing the application.
- Jenkins for CI / CD.
- Git for version control (Jenkins must use this git repository).

## Software Requirements
- Docker
- Jenkins


This README will not dicuss the installation steps of these softwares.

## Instructions to Run
With Jenkins:
1.  Make sure software requirements are fulfilled before runing the project.
2.  Spin up Jenkins. Commands may vary by OS to OS. However, if you are on Mac, you can do:
    brew services start jenkins-lts
3.  Access Jenkins (default localhost:8080). Login via admin or create a user.
4.  Inside Jenkins, docker plugins need to be installed.
    Goto manage Jenkins -> Plugins -> Available Plugins.
    Search for Docker. Choose "Docker" and "Docker Pipeline".
    Click on save and let it download.
5.  Create a new item, choose pipeline and give it a name. In Pipeline section, choose Pipeline script from SCM. Put in https://github.com/eshaanrathi2/resume-website.git
6.  Once pipeline is created, click on build. One can see the results in Jenkins console.
7. Test cases validate if website is up, git branch, date and time.
8. Exception handling is used to handle errors and edge cases. Standard test design patterns were not applied as focus was on to orchestrate the technologies and not API testing.

Without Jenkins (directly with Docker):
1. Clone the repository with
    git clone https://github.com/eshaanrathi2/resume-website.git
2. Go into the the repository that was cloned above
    cd resume-website
2. Build image and start container
    docker-compose up --build
3. Cleanup
    docker-compose down
1. Clone the repository with
    git clone https://github.com/eshaanrathi2/resume-website.git
2. Go into the the repository that was cloned above
    cd resume-website
2. Build image and start container
    docker-compose up --build
3. Cleanup
    docker-compose down

<!-- - To build image and start the containers:
    docker-compose up --build

- To stop the application and remove containers:
    docker-compose down

- TO start Jenkins:
    cd jenkins-config
    docker build -t jenkins-image .


    docker run -d \
    -p 8080:8080 \
    -v jenkins_home:/var/lib/jenkins \  # Adjust the volume path if needed
    -v /var/run/docker.sock:/var/run/docker.sock \  # Optional: adjust based on your needs
    my-jenkins-image


    docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11

    docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11 -->

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
