node {

	stage('checkout SCM'){
		git branch : 'main', url: 'https://github.com/kumaranilbhati/MyAngular.git'
	}

	stage('Build Docker Images'){
		bat 'docker-compose build'
	}

	// stage('Stop Container If Running'){
	// 	stdout = bat(returnStdout:true , script: 'docker ps -q -f status=running -f name=angular-app').trim()
	// 	result = stdout.readLines().drop(1).join("")
	// 	if(result?.trim()){
	// 		echo "One running Container ${result} found for the same image."
	// 		bat 'docker container stop angular-app'
	// 		echo 'Above container stopped.'
	// 		bat 'docker rm angular-app'
	// 		echo 'Above container removed.'
	// 	}
	// 	else{
	// 		echo 'No running Container found.'
	// 	}
	// }
	stage('Dockore compose up'){
		bat 'docker-compose up -d'
		echo 'Application is up on http://localhost:81.'
	}
}