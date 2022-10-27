node {
  // JDK 8 사용하도록 설정하기
  stage 'Setting'
  def javaHome = tool name: 'jdk8', type: 'hudson.model.JDK'
  env.JAVA_HOME = "${javaHome}"
  env.PATH = "${env.PATH}:${env.JAVA_HOME}/bin"

  // github에서 소스 얻어오기
  stage 'Checkout'
  git branch: 'development', credentialsId: '{your credential id}', url: '{your git url}'

  // Maven으로 빌드 실행하기
  stage 'Build'
  def mvnHome = tool 'M3'
  sh "${mvnHome}/bin/mvn -P local -Dmaven.test.skip=true -Ddeploy-path=./deploy clean install"

  // 테스트 진행하기
  stage 'Test'
  sh "${mvnHome}/bin/mvn -P local -B -Dmaven.test.failure.ignore verify"
  step([$class: 'JUnitResultArchiver', testResults: '**/target/surefire-reports/TEST-*.xml'])

  // 정적 검사 수행
  stage 'Analysis'
  sh "${mvnHome}/bin/mvn site"
  step([$class: 'CheckStylePublisher', canComputeNew: false, defaultEncoding: '', healthy: '', pattern: '**/checkstyle-result.xml', unHealthy: ''])
  step([$class: 'FindBugsPublisher', canComputeNew: false, defaultEncoding: '', excludePattern: '', healthy: '', includePattern: '', pattern: '**/findbugsXml.xml', unHealthy: ''])
  step([$class: 'PmdPublisher', canComputeNew: false, defaultEncoding: '', healthy: '', pattern: '**/pmd.xml', unHealthy: ''])

  // 패키지 저장
  step([$class: 'ArtifactArchiver', artifacts: '**/target/*.jar', fingerprint: true])
}