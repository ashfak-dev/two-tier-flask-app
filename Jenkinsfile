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
                sh 'cd /root/two-tier-flask-app && docker compose down || true'
                sh 'cd /root/two-tier-flask-app && docker compose up -d --build'
            }
        }

        stage('Check Running Containers') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful. Flask app is live on port 5000.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
