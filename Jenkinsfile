pipeline {
    agent any 

    stages {
        
        stage('Check Python') {
            steps {
              bat 'python --version'
            }
}

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t jenkins-test-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker rm -f jenkins-container || exit 0'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name jenkins-container jenkins-test-app'
            }
        }
    }
}

