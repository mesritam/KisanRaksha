pipeline {
    agent any
    stages {
        stage('Install') {
            steps { sh 'python3 -m pip install -r requirements.txt' }
        }
        stage('Test') {
            steps { sh 'pytest -q' }
        }
        stage('Docker Build') {
            steps { sh 'docker build -t ai-automation-api:${BUILD_NUMBER} .' }
        }
    }
}
