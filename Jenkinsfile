pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/tanish-pat/jktut'
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
