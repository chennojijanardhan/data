pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t my-rest-api:latest .'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker rm -f my-rest-api || exit 0
                docker run -d -p 8081:8080 --name my-rest-api my-rest-api:latest
                '''
            }
        }

        stage('API Test - Hello') {
            steps {
                bat '''
                echo Running Postman tests for /hello
                newman run postman_collection.json ^
                  --env-var baseUrl=http://localhost:8081
                '''
            }
        }
    }
}
