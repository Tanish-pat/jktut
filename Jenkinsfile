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
                // Set up Python environment and install dependencies
                'python -m venv venv'
                'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest
                'venv\\Scripts\\pytest test\\test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                // Run the Flask app (you may replace this with deployment-specific steps)
                'venv\\Scripts\\python app.py'
            }
        }
    }
}
