# Housing and communal services



## Quikstart due to [Airflow official docs](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)

### Initializing Environment
Before starting Airflow for the first time, 
you need to prepare your environment, i.e. create the necessary files, 
directories and initialize the database.


### Steps:

1.  ### for Linux
```shell
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
1.  ### for Windows
Manually create .env file in the same folder as docker-compose.airflow.localyaml with this content to get rid of the warning:  
AIRFLOW_UID=5000


2. ### Init database. Here the account with login "airflow" and the password "airflow" will be created.

```shell
docker-compose up airflow-init
```
3. ### Run this
```shell
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml'

```
3. ### Or this
```shell
docker-compose -f docker-compose.aiflow.local.yml up -d --build


```
4. ### After all you should see this: 
```shell
$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                    PORTS                    NAMES
21f73e11f9e6   apache/airflow:2.5.1   "/usr/bin/dumb-init …"   44 minutes ago   Up 44 minutes (healthy)   8080/tcp                 housing-and-communal-services_airflow-scheduler_1
5001a6f6e1df   apache/airflow:2.5.1   "/usr/bin/dumb-init …"   44 minutes ago   Up 44 minutes (healthy)   8080/tcp                 housing-and-communal-services_airflow-worker_1
c804f961acfa   apache/airflow:2.5.1   "/usr/bin/dumb-init …"   44 minutes ago   Up 44 minutes (healthy)   8080/tcp                 housing-and-communal-services_airflow-triggerer_1
4762eacb8974   apache/airflow:2.5.1   "/usr/bin/dumb-init …"   44 minutes ago   Up 44 minutes (healthy)   0.0.0.0:8080->8080/tcp   housing-and-communal-services_airflow-webserver_1
44664cbd850d   postgres:13            "docker-entrypoint.s…"   46 minutes ago   Up 46 minutes (healthy)   0.0.0.0:5432->5432/tcp   housing-and-communal-services_postgres_1
de303352f0e0   redis:latest           "docker-entrypoint.s…"   46 minutes ago   Up 46 minutes (healthy)   6379/tcp                 housing-and-communal-services_redis_1
```
