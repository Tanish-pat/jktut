pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/Tanish-pat/jktut'
            }
        }
        stage('Setup Venv') {
          steps {
            script {
              sh 'C:/Program Files/Git/bin/sh.exe -c "python -m venv venv"'
              sh 'C:/Program Files/Git/bin/sh.exe -c "source venv/Scripts/activate"' 
            }
          }
        }
        stage('Install Dependencies') {
            steps {
                // Set up Python environment and install dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest
                sh 'python test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                // Run the Flask app (you may replace this with deployment-specific steps)
                sh 'python app.py'
            }
        }
    }
}
