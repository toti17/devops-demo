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
                    echo 'building docker file'
                    
                '''
                def customImage = docker.build("my-image:${env.BUILD_ID}")
                customImage.inside {
                    sh 'python demo.py'
                }
            }
        }
    }
}