# project_dashboard

## To Clone
```
git clone https://github.com/Rohit-Thakre/project_dashboard.git
```

## After cloning Run The code using in cmd
```
python manage.py runserver 
```

## In your can Db might be missing so create you may need to run 
```
python manage.py makemigrations

python manage.py runserver 
```

## Create a superUser as needed using this command
```
python manage.py createsuperuser
```
## Here is api path 
http://127.0.0.1:8000/api/data/


## To Create Db from Json
TO accomplish this you will need Postman.exe
feed the json data to this end point after running the server, the db will create it by itself.
```
http://127.0.0.1:8000/read_json/
```


