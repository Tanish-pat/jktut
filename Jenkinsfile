pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/tanish-pat/jktut'
            }
        }
        // stage('Setup Venv') {
        //     steps {
        //         // Set up Python environment and install dependencies
        //         sh 'python -m venv venv'
        //         sh 'venv\\Scripts\\activate'
        //     }
        // }
        // stage('Install Dependencies') {
        //     steps {
        //         // Set up Python environment and install dependencies
        //         sh 'pip install -r requirements.txt'
        //     }
        // }

        // stage('Run Tests') {
        //     steps {
        //         // Run pytest
        //         sh 'python test_app.py'
        //     }
        // }

        stage('Deploy') {
            steps {
                // Run the Flask app (you may replace this with deployment-specific steps)
                bat 'python.exe app.py'
            }
        }
    }
}
