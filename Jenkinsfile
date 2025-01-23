pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/Tanish-pat/jktut'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Set up Python environment
                sh 'python -m venv venv'
                sh './venv/Scripts/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest
                sh './venv/Scripts/pytest test/test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                // Run the Flask app (replace with actual deployment steps)
                sh 'python app.py'
            }
        }
    }
}
