pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/tanish-pat/jktut'
            }
        }
        stage('Setup Venv') {
            steps {
                // Set up Python environment and install dependencies
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Set up Python environment and install dependencies
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest
                bat 'python test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                // Run the Flask app (you may replace this with deployment-specific steps)
                bat 'python app.py'
            }
        }
    }
}
