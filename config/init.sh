#!/bin/bash

source ../settings/private_config.py

echo "DB setup"
echo "grant select,insert,delete,update,create,drop,file, alter,index on *.* to ${DB_USER}@localhost identified by '${DB_PASS}';" | mysql -uroot -p
echo "DROP DATABASE IF EXISTS ${DB_NAME};" | mysql -u${DB_USER} -p${DB_PASS}
echo "CREATE DATABASE ${DB_NAME} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql -u${DB_USER} -p${DB_PASS}

# default db
python ../manage.py syncdb --noinput
python ../manage.py migrate
python ../manage.py importcsv

echo 'master data'
