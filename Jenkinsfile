
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building IT Service Desk Application'
                bat 'python --version'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Automated Test Cases'
                bat 'python -m pytest test_service_desk.py -v --junitxml=report.xml'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Application is ready for deployment'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'report.xml'
        }

        success {
            echo 'BUILD SUCCESSFUL'
        }

        failure {
            echo 'BUILD FAILED - Check Console Output'
        }
    }
}
