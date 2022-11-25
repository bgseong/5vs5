pipeline{
    agent any

    environment{
        VERSION = "1.0"
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
