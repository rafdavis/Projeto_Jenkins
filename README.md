# Projeto_Jenkins

## Descrição:

O projeto tem como objetivo criar uma pipeline CI/CD utilizando as tecnologias FastAPI, Docker, Jenkins e Kubernetes. Fazendo a automação do deploy da aplicação no cluster Kubernetes local e o push da imagem da aplicação no Docker Hub.

## Tecnologias Utilizadas:

- FastAPI: Framework web em Python
- Docker: Para conteinerização da aplicação
- Docker Hub: Registro público de imagens
- Jenkins: Ferramenta de CI/CD
- Kubernetes local: Minikube, Docker Desktop

## Objetivos:

- Preparação do Ambiente
- Criar o Dockerfile e subir para o Docker Hub
- Criar o Deployment, Service e aplicá-los no cluster Kubernetes local
- Criar a pipeline no Jenkins para realizar o build e push da imagem Docker
- Configurar o Jenkins para acessar o cluster Kubernetes local e fazer o deploy no cluster.

## Etapa 1: Preparação do Ambiente para o Projeto

### Criação do repositório no GitHub

Acesse o [GitHub](https://github.com), selecione `New`

![](imgs/newRepositorio.png)

### Preencha as informações do seu repositório.

![](imgs/Repositorio.png)

### Após isso, crie o repositório e adicione a aplicação

## Criação da conta no Docker Hub

### Acesse o [Docker Hub](https://hub.docker.com), selecione `Sign up`

![](imgs/DockerHub.png)

### Após isso, realize o cadastro com as suas informações.

![](imgs/cadastroDockerHub.png)

## Instalar o Kubectl, Minikube, Java, Jenkins e Docker Desktop

### Kubectl:

- 1. Adicione as chaves e os repositórios necessários:

```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg

curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```

- 2. Adicione o repositório Kubernetes:

```bash
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list
```

- 3. Atualize os pacotes e instale o Kubectl:

```bash
sudo apt-get update
sudo apt-get install -y kubectl
```

### Minikube:

- Baixe os arquivos do Minikube e instale em seguida:

```
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```

### Para instalar o Jenkins é necessário o Java:

- 1. Atualize os pacotes e instale o Java JDK 17:

```bash
sudo apt update && sudo apt install openjdk-17-jdk -y
```

- 2. Com o Java instalado, adicione a chave do Jenkins ao sistema:

```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
```

- 3. Adicione o repositório do Jenkins:

```bash
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
```

- 4. Atualize os pacotes e instale o Jenkins:

```bash
sudo apt update && sudo apt install jenkins -y
```

- 5. Com o Jenkins instalado, visualize a senha inicial com o seguinte comando:

```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

### Docker Desktop:

- 1. Acesse [Docker Docs](https://https://docs.docker.com/desktop/setup/install/windows-install/) e selecione `Docker Desktop for Windows -x86_64`:

![](imgs/downloadDockerDesktop.png)

- 2. Entre no app e realize o login:

![](imgs/DockerDesktop.png)

- 3. Com o Docker Desktop instalado, adicione o usuário atual e do Jenkins ao grupo Docker:

```
sudo usermod -aG docker $USER
sudo usermod -aG docker jenkins
```

- 4. Reinicie o Jenkins para aplicar as permissões no Docker:

```
sudo systemctl restart jenkins
```

## Verifique o acesso ao cluster Kubernetes local:

### Com as tecnologias instaladas, inicie o Kubernetes local:

#### Configure o Docker como driver padrão:

```
minikube config set driver docker
```

#### Inicie o Kubernetes:

```
minikube start
```

![](imgs/minikubeStart.png)

#### Com o minikube iniciado, confira o acesso ao Kubernetes:

```
kubectl get svc
```

![](imgs/clusterLocal.png)