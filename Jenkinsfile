pipeline {
    agent any

    environment {
        VENV_DIR = 'venv' // Define a reusable variable for the virtual environment
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository
                git branch: 'main', url: 'https://github.com/tanish-pat/jktut'
<<<<<<< HEAD
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
=======
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                // Create and activate a Python virtual environment
                bat "python -m venv ${VENV_DIR}"
            }
        }
        stage('Install Dependencies') {
            steps {
                // Activate the venv and install dependencies
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
>>>>>>> 27f658d3797bcac5b5439ae5f149e658a6c5179d
            }
        }
        stage('Run Tests') {
            steps {
<<<<<<< HEAD
                // Run pytest
                bat 'python test_app.py'
=======
                // Activate venv and run tests
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                python test_app.py
                """
>>>>>>> 27f658d3797bcac5b5439ae5f149e658a6c5179d
            }
        }
        stage('Deploy') {
            steps {
<<<<<<< HEAD
                // Run the Flask app (you may replace this with deployment-specific steps)
                bat 'python app.py'
            }
        }
    }
}
=======
                // Activate venv and deploy Flask app
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                python app.py
                """
            }
        }
    }

    post {
        always {
            // Cleanup the virtual environment and workspace
            echo 'Cleaning up virtual environment and workspace...'
            bat "rmdir /S /Q ${VENV_DIR}" // Delete the virtual environment
            cleanWs() // Clean up the workspace
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed! Investigate the logs for issues.'
        }
    }
}
>>>>>>> 27f658d3797bcac5b5439ae5f149e658a6c5179d
