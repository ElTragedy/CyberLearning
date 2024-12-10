# Hello
not much here yet


# How to run
set up virtual env

#### macOS/Linux
`source venv/bin/activate`

#### Windows
`venv\Scripts\activate`

### install prereqs

`pip install -r requirements.txt`

### Install Postgresql
Version 17.2

### Test the env
go into the "cyberLearning" directory and run:
`python manage.py runserver`

### install postgres
You have to install postgres on your local machine to get the psql client
on your system. Please do that.

### Sync the database
pull repo and apply database changes `python manage.py migrate` to pull database 
structure. If you change it then use `makemigrations` to apply them.

### Run docker container
``` docker
docker run --name postgres-django -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=djangodb -p 5432:5432 -d postgres
```

docker run --name postgres-django \
  -e POSTGRES_USER=django_user \
  -e POSTGRES_PASSWORD=django_password \
  -e POSTGRES_DB=django_db \
  -p 5432:5432 \
  -v postgres_data:/var/lib/postgresql/data \
  -d postgres
