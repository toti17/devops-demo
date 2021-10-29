pipeline {
    agent { docker { image 'python:3.8.10'} }
    stages {
        stage('build') {
            steps {
                sh '''
                    python --version
                '''
            }
        }
        stage('test') {
            steps {
                sh '''
                    python3 src/demo_test.py
                '''
            }
        }
        stage('deploy') {
            steps {
                sh '''
                    docker --version
                    docker build -t devops-demo .
                '''
            }
        }
    }
}