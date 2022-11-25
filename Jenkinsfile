pipeline{
    agent any

    environment{
        VERSION = "t0.0.1"
    }
    stages {
        stage("build") {
            steps{
                sh "docker build --tag fastapi:${VERSION} ."
            }
        }
        stage("Run") {
            steps{
                sh "docker-compose up"
            }
        }
                
    }
}
