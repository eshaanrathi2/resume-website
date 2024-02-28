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
        stage('Start server and run tests') {
          steps {
            sh 'docker-compose up --build -d --no-color --wait'
            sh 'docker compose ps'
          }
        }
    }
    
    post {
        always {
          sh 'docker compose down --remove-orphans -v'
          sh 'docker compose ps'
        }
    }
}
