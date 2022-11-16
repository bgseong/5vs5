node {
    def hello = 'Hello bgsung' // 변수선언
    stage ('clone') {
        git credentialsId: 'bgs', url: 'https://github.com/bgseong/5vs5.git'
    }
    
    stage ('print') {
        print(hello) // 함수 + 변수 사용
    }
}
