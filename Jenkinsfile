pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/ashfak-dev/two-tier-flask-app.git'
            }
        }

        stage('Build and Start Containers') {
            steps {
                sh '''
		docker rm -f mysql-db flask-app || true
                docker compose down || true
                docker compose up -d --build
                '''
            }
        }

        stage('Check Running Containers') {
            steps {
                sh 'docker ps -a'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
