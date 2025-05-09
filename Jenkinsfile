pipeline {
    agent any

    environment {
        FTP_USER = 'ftpuser'  
        FTP_PASSWORD = 'Eldho' 
        FTP_TARGET_DIR = 'ftp://127.0.0.1/ftp_data'  
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/eldho1markose/product-microservice.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t product-microservice .'
                }
            }
        }

       stage('Save Docker Image to TAR') {
            steps {
                bat 'docker save -o product_microservice.tar product-microservice'
            }
        }

        stage('Upload to FTP') {
            steps {
                script {
                    bat '''
                    curl -T product_microservice.tar --user ftpuser:Eldho ftp://127.0.0.1/product_microservice.tar
                    '''
                }
            }
        }
    }
}
