pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/seu-usuario/cpf-validator.git'
            }
        }

        stage('Build Docker') {
            steps {
                bat 'docker build -t cpf-validator .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run cpf-validator pytest'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker run -d -p 5000:5000 --name cpf-validator-app cpf-validator'
            }
        }
    }

    post {
        always {
            bat 'docker stop cpf-validator-app || exit 0'
            bat 'docker rm cpf-validator-app || exit 0'
        }
    }
}