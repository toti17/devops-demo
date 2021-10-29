pipeline {
    agent none
    stages {
            agent { docker { image 'python:3.8.10'} }
        stage('build') {
            steps {
                sh '''
                    python --version
                '''
            }
        }
        stage('test') {
            agent { docker { image 'python:3.8.10'} }
            steps {
                sh '''
                    python3 src/demo_test.py
                '''
            }
        }
        stage('deploy') {
            agent { dockerfile true }
        }
    }
}