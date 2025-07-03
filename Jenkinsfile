pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    extensions: [],
                    userRemoteConfigs: [[
                        url: 'https://github.com/EvilasioJuniorUFC/cpf-validator.git',
                        credentialsId: '' // Adicione se for repositório privado
                    ]]
                ])
            }
        }

        stage('Build and Test') {
            steps {
                bat 'docker build -t cpf-validator .'
                bat 'docker run --name cpf-validator-test cpf-validator pytest'
                bat 'docker rm -f cpf-validator-test || exit 0'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker stop cpf-validator-app || exit 0'
                bat 'docker rm -f cpf-validator-app || exit 0'
                bat 'docker run -d -p 5000:5000 --name cpf-validator-app cpf-validator'
            }
        }
    }
}