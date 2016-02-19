#To run locally

  - make sure you have `postgresql` and `postgis`
  - `sudo su postgres`
  - `createdb -d moziodb -U deepankar` (create a user deepankar in postgres)
  - `psql -d moziodb -U deepankar`
  -  Inside the db console run sql `CREATE EXTENSION postgis;` and `CREATE EXTENSION postgis_topology;`
  -  exit postgres user (ctrl-D)
  - `git clone https://github.com/dbajpeyi/service_area.git`
  - `pip install -r requirements.txt`
  -  `cd service_area` && `python manage.py makemigrations`
  -  `python manage.py migrate`
  -  `python manage.py runserver`


#Docs :
http://docs.servicearea.apiary.io/

#Run tests

To run tests : `python manage.py test`
