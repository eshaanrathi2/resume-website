pipeline {
    agent any
    environment {
        PATH = "$PATH:/usr/local/bin" // or wherever Docker is installed
    }
    stages {
        stage("verify tooling") {
            steps {
                sh "docker --version"
            }
        }
        stage('Start container') {
          steps {
            sh 'docker-compose up --build'
            //sh 'docker compose ps'
          }
        }
    }  
}