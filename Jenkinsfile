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
            # Download the official pip installer script
            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            
            # Install pip for the current user
            python3 get-pip.py --user
            
            # Add the local bin to PATH so Jenkins can find 'pytest'
            export PATH=$PATH:$HOME/.local/bin
            
            python3 -m pip install pytest
            python3 -m pytest test_calculator.py
        '''
            }
        }
        stage('Package') {
            steps {
                sh 'python3 setup.py bdist_wheel'
            }
        }
    }
}
