django-server
-------------
|Build Status|
|Codacy Quality Badge|
|Codacy Coverage Badge|

The API server for accessing content across the ASWWU websites. Built with Django 2, the Django REST Framework, and
Python 3.7.

Local Deployment
----------------
Use these steps to setup your local developemnt environment.

MySQL
+++++
MySQL can be installed with Brew (not recommended), MAMP (easy but big), or Docker (hard but lightweight). Use MySQL
version 5.7.22.

Brew
....
1. Install with brew

::

  $ brew install mysql

2. Save yourself a lot of pain and skip to the Docker section

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

2. Enter the MySQL command line, you may need to restart the container first

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
  mysql> CREATE DATABASE mask CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  mysql> CREATE DATABASE pages CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;



Django Setup
++++++++++++
1. Install dependencies. NOTE: mysqlclient can cause issues on Mac. Ensure that you installed mysql with brew

::

  $ pipenv install

2. Run migrations

::

  $ pipenv run python manage.py migrate

3. Run server

::

  $ pipenv run python manage.py runserver


.. |Build Status| image:: https://travis-ci.org/ASWWU-Web/django-server.svg?branch=develop
    :target: https://travis-ci.org/ASWWU-Web/django-server

.. |Codacy Quality Badge| image:: https://api.codacy.com/project/badge/Grade/dc03c99f843342e895b1a861ad2ec0f7
    :target: https://www.codacy.com/project/aswwuwebmaster/django-server/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ASWWU-Web/django-server&amp;utm_campaign=Badge_Grade_Dashboard

.. |Codacy Coverage Badge| image:: https://api.codacy.com/project/badge/Coverage/dc03c99f843342e895b1a861ad2ec0f7
    :target: https://www.codacy.com/app/aswwuwebmaster/django-server?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ASWWU-Web/django-server&amp;utm_campaign=Badge_Coverage
