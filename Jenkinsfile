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
                sh 'docker build -t cpf-validator .'
                sh 'docker run --name cpf-validator-test cpf-validator pytest'
                sh 'docker rm -f cpf-validator-test || exit 0'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker stop cpf-validator-app || exit 0'
                sh 'docker rm -f cpf-validator-app || exit 0'
                sh 'docker run -d -p 5000:5000 --name cpf-validator-app cpf-validator'
            }
        }
    }
}
