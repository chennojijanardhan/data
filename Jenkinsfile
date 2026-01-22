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
                sh 'docker build -t my-rest-api:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f my-rest-api || true
                docker run -d -p 8081:8080 --name my-rest-api my-rest-api:latest
                '''
            }
        }

        stage('API Test - Hello') {
            steps {
                sh '''
                echo "Running Postman health check via Newman"
                newman run postman_collection.json \
                  --env-var baseUrl=http://localhost:8081
                '''
            }
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Jenkinsfile detected successfully!'
            }
        }
    }
}
