pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh 'pytest test_calculator.py'
            }
        }
        stage('Package') {
            steps {
                sh 'python3 setup.py bdist_wheel'
            }
        }
    }
}
