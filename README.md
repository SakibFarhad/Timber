# Project Timber

It is a docker application I made for practice.

It containes 4 container

* app_container
* mongodb_container
* mqtt_container
* mongo_express_container


app container has two python app 

* app
* glue-app

`app` generates prime number within a range and publishes it to mqtt_container.  
`glue-app` subcribes to mqtt_container and gets the data to insert it into the mongo_container

To run this application you will need `docker-compose`

```bash
docker-compose up -d
```
After build you will find following running containers with `docker ps -a` command

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                      NAMES
626bc0b9a0ac        mongo-express       "tini -- /docker-ent…"   4 minutes ago       Up 4 minutes        0.0.0.0:85->8081/tcp       mongo_express_container
eaefb3d5c192        mongo               "docker-entrypoint.s…"   10 minutes ago      Up 5 minutes        0.0.0.0:32808->27017/tcp   mongodb_container
d7b281c67298        timber_app          "/usr/local/bin/pyth…"   10 minutes ago      Up 5 minutes                                   app_container
c615d5d9c1bf        eclipse-mosquitto   "/docker-entrypoint.…"   10 minutes ago      Up 5 minutes        0.0.0.0:32807->1883/tcp    mqtt_container
```

To run the app you will need to go inside the `app_container`

```bash
docker exec -it app_container /bin/bash
```

run:

```bash
python app/main.py 5 10
```

also this command will work to run it from out side the container

```bash
docker exec -it app_container python app/main.py 5 20
```

now if you go to your browser at [http://localhost:85](http://localhost:85)  

you will see the data bases we created along with the data. 