pipeline {
  agent any
  stages {
    // stage("Initialize") {
    //     steps {
    //         script {
    //             def dockerHome = tool 'docker'
    //             env.PATH = "${dockerHome}/bin:${env.PATH}"
    //         }
    //     }
    // }
    stage("verify tooling") {
      steps {
        sh '''
          docker version
          docker info
          docker compose version 
          curl --version
        '''
      }
    } 
  }  
}
