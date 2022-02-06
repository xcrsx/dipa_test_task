# Dipa_messages

Test task for python developer

---

## requirements

- [Django](https://github.com/django/django)
- [psycopg2](https://github.com/psycopg/psycopg2)
- [poetry](https://github.com/python-poetry/poetry)
- [Docker](https://docs.docker.com/get-docker/)

---

## Getting started

1. Create `.env` file and fill it with the data, according to `.env.example` file.
2. To build the docker image run the command `sudo docker-compose build`.
3. To create all model tables in the database run the command `sudo docker-compose run web python manage.py migrate`.
4. To create admin run the command `sudo docker-compose run web python manage.py createsuperuser` and enter your desired username, password, etc.

## running

To start the service run the command `sudo docker-compose up`.

Now, open a web browser and go to http://localhost:8000. 

To administrate from admin site go to http://localhost:8000/admin/.

To stop the service press `ctrl + c`.