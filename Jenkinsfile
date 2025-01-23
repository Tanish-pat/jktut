pipeline {
    agent {
        docker {
            image 'ubuntu:latest' # Use a suitable Ubuntu image
        }
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Tanish-pat/jktut'
            }
        }
        stage('Setup Venv') {
            steps {
                sh 'python3 -m venv venv' 
                sh 'source venv/bin/activate'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                sh 'python app.py' 
            }
        }
    }
}
