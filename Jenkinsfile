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
                sh '''
            python3 -m pytest test_calculator.py
        '''
            }
        }
        stage('Package') {
            steps {
                echo 'Packaging into Wheel file...'
                // Install 'build' to create the wheel
                sh 'pip install build'
                // Generates the .whl file inside the /dist folder
                sh 'python3 -m build --wheel'
                
                // Optional: Verify the file exists
                sh 'ls -l dist/'
            }
        }
    }
}
