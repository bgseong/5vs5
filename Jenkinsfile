pipeline{
    agent any

    environment{
        VERSION = "1.0"
    }
    stages {
        stage("build") {
            sh "docker build --tag fastapi:${VERSION}"
        }
        stage("Run") {
            sh "docker run --rm -p 8080:8000 fastapi:${VERSION}"
        }
    }
}
