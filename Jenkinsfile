
pipeline {
    agent any

    triggers {
            pollSCM('H/2 * * * *')
        }

    stages {
        stage('Build') {
            steps {
                sh 'mkdir -p dist'
                sh 'python3 -m zipfile -c dist/calculator.zip src'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Deploy') {
            steps {
                sh 'cp dist/calculator.zip /cargo/'
            }
        }
    }
}

