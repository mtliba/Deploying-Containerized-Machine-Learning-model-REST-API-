# Deploying-Containerized-Machine-Learning-model-REST-API-
Deploying  ML model into production using Nginx web server , Gunicorn, Flask ,dockercompose
Variants SVM models trained on iris dataset are Containerized within flask in app service, Containerized Nginx web server 
as a reverse proxy for Gunicorn in server service , both services are bounded together in local using dockercompose .
Gunicorn used to serve the falsk app , in order to run first clone this repository and run svp.py four pkl files will be 
saved within same file folder then run the following :

```shell
$ docker-compose up --build
```

Machine Learning app is up and running, accepting requests on port 8080 and ready to serve , send request by curl or by runnig 
request.py if you chose to run request.py install request first .
```shell
$ pip install request 
$ python request.py

```
as mentioned four SVM algorithm are trained ('SVC with linear kernel': noted in URL as SVC, 'LinearSVC (linear kernel)': noted in URL as LinearSVC,
'SVC with RBF kernel': noted in URL as SVC-RBF ,'SVC with polynomial (degree 3) kernel': noted in URL as SVC-Pd3 )
run SVC-Pd3 :
 
 ```shell
$ curl -H "Content-Type: application/json" --request POST --data'[{"sepal_length":6.1,"sepal_width":2.5,"petal_length":3.8,"petal_width":2.1}]' http://localhost:8080/predict?model=SVC-Pd3

```

