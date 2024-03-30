pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'muhammadahmedsuhail/mlops-a-1:final'
    }

    stages {
        stage('Building Image') {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE_NAME ."
                }
            }
        }

        stage('Pushing Image') {
            environment {
                DOCKER_HUB_CREDENTIALS = credentials('dockerhub-credentials')
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        sh "echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin"

                        sh "docker push $DOCKER_IMAGE_NAME"
                    }
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -af'
        }
        success {
            echo 'Pipeline Success'
            mail bcc: '', body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "Success ${env.JOB_NAME}", to: "muhammadahmedsuhail@gmail.com";
        }
        failure {
            echo 'Pipeline Failed'
            mail bcc: '', body: "<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR ${env.JOB_NAME}", to: "muhammadahmedsuhail@gmail.com";
        }
    }
}
