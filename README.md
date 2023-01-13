  #  Flask
  
Example of microservice in **Python** using **Flash mini-framework** **dockerized** and deployed to **Kubernetes** with helm template

### Prerequisities 

> Install python3 

> Install Venv 
    
   
   See documentation [virtual environment](https://docs.python.org/3/library/venv.html)

    python3 -m venv virtual-env
  
  It is important to isolate the project 
   

> Use VSCode 

Install extension for python

> Flask

See documentation [Flask](https://flask.palletsprojects.com/en/2.2.x/)

    pip3 install Flask
  #  Flask
  
Example of microservice in **Python** using **Flash mini-framework** **dockerized** and deployed to **Kubernetes** with helm template

### Prerequisities 

> Install python3 

> Install Venv 
    
   
   See documentation [virtual environment](https://docs.python.org/3/library/venv.html)

	   python3 -m venv virtual-env
  
  It is important to isolate the project 
   

> Use VSCode 

Install extension for python

> Flask

See documentation [Flask](https://flask.palletsprojects.com/en/2.2.x/)

	   pip3 install Flask
	

> Freeze dependencies at the moment inside a requirements.txt file

		pip3 freeze > requirements.txt

> Install minikube

### STEP 

 1. Install dependencies `pip3 install -r requirements.txt`
 2. Start minikube `minikube start `
 3. Put docker daemons inside minikube `eval $(minikube -p minikube docker-env)
 4. Execution 
	 A) *Docker*
	 
		docker build -t webflask:1.0 .  
		docker run -d -p 80:5000 --name webe webflask:1.0
		minikube ip
     
     B) *Docker compose*
     
		    docker compose up -d 
		    minikube ip
	 
	 C)  *Kubernetes* 
			
		    kubectl apply -f deployment.yaml
 			kubectl apply -f service.yaml
 			kubectl get po,svc
 			minikube ip
 	
 	D) *Helm* 
		   

		    helm create webflask 
			helm template webflask   
			helm install webflask webflask/
	 


