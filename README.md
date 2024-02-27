## Tech used
- Apache httpd server for hosting source code.
- Docker for containerizing the app. Dockerfile and docker-compose to build image and container.
- Python to create mock API.
- make file for running everything.
- Git for version control.

## Requirements
- Docker
- Python3
- Python specific requirements (flask, pygit2) can be installed by
pip install -r requirements.txt


# resume-website
Run the commands to build and run the Docker image:
$ docker build -t httpd_1 .
$ docker run -dit --name my-running-app -p 80:80 httpd_1
<!-- docker run -it --rm --cpus 4 --memory 3G -v  -->


docker-compose build --no-cache
docker-compose up -d 
docker-compose down


Build and run together:
docker-compose up --build