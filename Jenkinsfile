pipeline {
    agent { docker { image 'python:3.5.1'} }
    stages {
        stage('build') {
            steps {
                sh '''
                    python --version
                    pip3 install pytest
                '''
            }
        }
        stage('test') {
            steps {
                sh '''
                    python3 -m pytest test/demo_test.py
                '''
            }
        }
    }
}