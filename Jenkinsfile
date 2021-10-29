pipeline {
    agent { docker { image 'python:3.5.1'} }
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
            agent any
            steps {
                sh '''
                    docker build -t devops-demo .
                '''
            }
        }
    }
}