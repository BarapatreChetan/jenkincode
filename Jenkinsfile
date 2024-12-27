pipeline {
    agent any
    stages {
        stage ("CheckOutCode") {
            steps {
                git url:'https://github.com/BarapatreChetan/jenkincode.git', branch:'main'
            }
        }
        stage ("Build Docker Image") {
            steps {
                sh 'docker build -t myimage .'
            }
        }
        stage ("Create Container") {
            steps {
                sh 'docker run -d -p 8501:8501 myimage'
            }
        }
    }
}