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
               sh '''
                    export PATH=$PATH:$HOME/.local/bin
                    python3 -m pip install build
                    
                    # Build the wheel (creates dist/calculator-1.0.0-py3-none-any.whl)
                    python3 -m build --wheel
                    
                    # Rename to the specific name requested: calculator-1.0.0.whl
                    mv dist/calculator-1.0.0-*.whl dist/calculator-1.0.0.whl
                    
                    ls -l dist/
                '''
            }
        }
    }
}
