pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    dockerbuild = docker.build("rafdavis/fastapi:${env.BUILD_ID}", '-f ./backend/Dockerfile ./backend')
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        dockerbuild.push('latest')
                        dockerbuild.push("${env.BUILD_ID}")}
                }
            }
        }

        stage('Scan Docker Image') {
            steps {
                script {
                    def trivyOutput = sh(script: "trivy image $APP_NAME:latest", returnStdout: true).trim()
                    println trivyOutput
                    if (trivyOutput.contains("Total: 0")) {
                        echo "Não foram encontradas vulnerabilidades nessa Imagem Docker"
                    } else {
                        echo "Foram encontradas vulnerabilidades nessa Imagem Docker"
                    }
                }
            }
        }

        stage('Deploy no Kubernetes') {
            environment {
                tag_version = "${env.BUILD_ID}"
            }
            steps {
                script {
                    withKubeConfig([credentialsId: 'kubeconfig']) {
                        sh "sed -i 's/{{tag}}/${tag_version}/g' ./k8s/deployment.yaml"
                        sh 'kubectl apply -f ./k8s/'
                    }
                }
            }
        }
    }
}