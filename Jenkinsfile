pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Tanish-pat/jktut.git' // Replace with your repo URL
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('flask-project:latest')
                }
            }
        }
        stage('Run Tests') {
            steps {
                sh 'echo "No tests for this project yet!"' // Add actual tests here
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 flask-project:latest'
                }
            }
        }
    }
}
