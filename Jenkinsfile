pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh '''
                    python3 --version
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
    }
}