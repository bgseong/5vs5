echo "start build"
node{
    def filename = 'backend'
    stage ('start') {
        if (filename.exist()) {
            mkdir filename
        }
        dir (filename) {
            stage('clone') {
                git 'https://github.com/bgseong/5vs5.git'
            }
        }
        state ('end') {
            echo "end build"
        }
    }
    
}
