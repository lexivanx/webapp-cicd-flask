pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "my_flask_app:${GIT_COMMIT}"
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
                sh 'docker save -o my_flask_app.tar $DOCKER_IMAGE'
                archiveArtifacts artifacts: 'my_flask_app.tar', fingerprint: true
            }
        }
        stage('Test') {
            steps {
                sh 'docker run --rm -v $(pwd)/tests:/app/tests $DOCKER_IMAGE pytest /app/tests'
            }
        }
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                // You can use the Docker plugin to push the image to a registry, e.g., Docker Hub, AWS ECR, or GCR
                // You can then deploy the container to a cloud provider or your on-premises infrastructure
                // The deployment process will depend on your chosen target environment
                sh 'echo "Deploying $DOCKER_IMAGE"'
            }
        }
    }
}
