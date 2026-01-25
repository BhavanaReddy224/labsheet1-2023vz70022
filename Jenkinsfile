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
            # 1. Ensure pip is available for this stage
            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            python3 get-pip.py --user
            export PATH=$PATH:$HOME/.local/bin
            
            # 2. Install the build tool
            python3 -m pip install --user build
            
            # 3. Run the build
            # This requires a pyproject.toml or setup.py in your root directory
            python3 -m build --wheel
            
            # 4. Verify the output
            ls -l dist/
        '''
            }
        }
    }
}
