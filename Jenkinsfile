
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building IT Service Desk Application'
                bat '"C:\\Users\\psaik\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" --version'
                bat '"C:\\Users\\psaik\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Automated Test Cases'
                bat '"C:\\Users\\psaik\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pytest test_service_desk.py -v --junitxml=report.xml'
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
            junit allowEmptyResults: true, testResults: 'report.xml'
        }
        success {
            echo 'BUILD SUCCESSFUL'
        }
        failure {
            echo 'BUILD FAILED - Check Console Output'
        }
    }
}
