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
            steps {
                sh '''
                    echo 'creating docker file'
                    
                '''
                agent {
                    docker {
                        docker build -t demo .
                    }
                }
            }
        }
    }
}