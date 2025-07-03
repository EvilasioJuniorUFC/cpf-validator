pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t cpf-validator .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run cpf-validator pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 --name cpf-validator-app cpf-validator'
            }
        }
    }
}