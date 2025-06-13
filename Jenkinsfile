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
                    def imageName = "rafdavis/fastapi:latest"
                
                echo "Escaneando imagem com Trivy: ${imageName}"
                def trivyOutput = sh(script: "trivy image --exit-code 1 --severity CRITICAL,HIGH ${imageName}", returnStatus: true)

                if (trivyOutput == 0) {
                    echo "✅ Sem vulnerabilidades críticas ou altas na imagem Docker"
                } else {
                    echo "❌ Vulnerabilidades CRÍTICAS ou ALTAS foram encontradas!"
                    error("Falha de segurança detectada pela varredura do Trivy")
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