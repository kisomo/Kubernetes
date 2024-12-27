'''
get all the functionalities
kubectl 

get your cluster info
kubectl cluster-info

get available nodes
kubectl get nodes

check details of a particular node like minikube for example
kubectl describe node minikube 

take down a particular cluster (iris for example) - disable scheduling
kubectl cordon iris

bring back the cluster (assume cluster name is iris)
kubectl uncordon iris 

get namespaces
kubectl get namespace 

create a new namespace called muthoka
kubectl create namespace muthoka

delete namespace called muthoka
kubectl delete namespace muthoka

create a namespace using yaml file, open a yaml file put the required entries and run
kubectl create -f namespace-terrence.yaml

see the details of your newly created namespace
kubectl describe namespace terrence 

created our first kubernetes application. from the default namespace
kubectl get pods

you can also chect the pods in a particular namespace
kubectl get pods -n dev 
kubectl get pods -n muthoka-prod

you can also set your default namespace to what you want
kubectl config set-context --current --namespace=muthoka-prod

create our first deployment - use the default hello world container application
kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4

you can the pods in all the namespaces
kubectl get pods --all-namespaces

get events in a particular namespace or in all namespaces
kubectl get events -n muthoka-test
kubectl get events --all-namespaces

get services in a particular namespace or in all namespaces
kubectl get services -n muthoka-test
kubectl get services --all-namespaces

get deployments in a particular namespace or in all namespaces
kubectl get deployments -n muthoka-test
kubectl get deployments --all-namespaces

is pods the same thing as deployments ????

you need a service to access the pod
create a deployment service on hello-node and set it at type loadbalancer on port 8080
kubectl expose deployment hello-node --type=LoadBalancer --port=8080

now check the services and you will see the hello-node service that you just created
kubectl get services

now lets forward connection to this loadbalancer so we can access the service. in a cloud environment you don't need to do this.
you will just need elastic load balancer in AWS for example. open a new terminal and run this command
minikube service hello-node

=======================================================
deploy the first yaml file????? yes, the first yaml file has type "deployment"
kubectl apply -f solution/v1.yaml

check the deployments
kubectl get deployments.apps

deployments also create pods and replica sets, so lets check on those
kubectl get replicasets
kubectl get pods

get details of one of the pods you just created
kubectl describe pods <POD NAME>

get details of the deployment you just created
kubectl describe deployments <DEPLOYMENT NAME>

and this is how you delete these resources
kubectl delete -f solution/v1.yaml

==============================================================================
The second yaml file is service loadbalancer added to the deployment of the first yaml file
kubectl apply -f solution/v2.yaml

now we can look at the replicasets and the pods created like we did previously but we can now at the services
kubectl get services

to forward traffic to this load balancer we do just like we did for the deployment, open a new terminal and run
minikube service mywebapp

==============================================================================
the third yaml file is config map and scaling - we have added a configuration map on top so now we have deployment, service 
and config map. we have also set the replicas to five. for the config map we are just sending some ENV variables to change some
background colors but you can make this more sophisticated.
kubectl apply -f solution/v3.yaml

check to confirm the 5 new pods have been created
kubectl get pods


============================================================================
the fourth yaml file is for resource limits, set minimum and maximum usage for memory and cpu.
kubectl apply -f solution/v4.yaml

check the deployments to see the limits you have set
kubectl describe deployments mydeployment

'''


'''
get logs so you can trouble shoot your containers
kubectl logs -l app=mywebapp

to follow along continous add the f flag
kubectl logs -f -l app=mywebapp

'''