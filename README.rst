django-server
-------------
The API server for accessing content across the ASWWU websites. Built with Django 2, the Django REST Framework, and
Python 3.7.

Local Deployment
----------------
Use these steps to setup your local developemnt environment.

MySQL
+++++
MySQL can be installed with MAMP (easy but big) or Docker (hard but lightweight). Use MySQL version 5.7.22.

MAMP
....
1. Download and install MAMP

2. Start servers

3. Skip to database setup

Docker
......

1. Install MySQL server

::

  $ docker run -d \
    -p 8889:3306 \
    -e MYSQL_ROOT_PASSWORD=root \
    --name=mysql-server \
    mysql/mysql-server:5.7.22

2. Enter the MySQL command line

::

  $ docker exec -it mysql-server mysql -uroot -proot

3. Give the root user permission on localhost

::

  mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root';

Database Setup
..............
1. Create the databases, use Docker step 2 to enter the MySQL command line if necessary

::

  mysql> CREATE DATABASE django CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  mysql> CREATE DATABASE elections CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  mysql> CREATE DATABASE jobs CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  mysql> CREATE DATABASE pages CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  mysql> CREATE DATABASE people CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;



Django Setup
++++++++++++
1. Install dependencies

::

  $ pipenv install

2. Run migrations

::

  $ pipenv run python manage.py migrate

3. Run server

::

  $ pipenv run python manage.py runserver
