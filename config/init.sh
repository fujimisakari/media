#!/bin/sh

source ../settings/private_config.py

# 本番環境用
if [ $1 -a $1 = 'init' ]; then
    echo "DB setup"
    echo "grant select,insert,delete,update,create,drop,file, alter,index on *.* to ${DB_USER}@localhost identified by '${DB_PASS}';" | mysql -uroot -p
    echo "DROP DATABASE IF EXISTS ${DB_NAME};" | mysql -u${DB_USER} -p${DB_PASS}
    echo "CREATE DATABASE ${DB_NAME} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql -u${DB_USER} -p${DB_PASS}

    # default db
    python ../manage.py syncdb --noinput
    python ../manage.py migrate

    echo 'master data'

fi

# dev環境用
if [ $1 -a $1 = 'dev' ]; then

    # pip
    if [ $2 -a $2 = 'pip' ]; then
        echo 'pip install'
        pip install -r pip_list
    fi

    echo "DB setup"
    echo "grant select,insert,delete,update,create,drop,file, alter,index on *.* to ${DB_USER}@localhost identified by '${DB_PASS}';" | mysql -uroot -p
    echo "DROP DATABASE IF EXISTS ${DB_NAME};" | mysql -u${DB_USER} -p${DB_PASS}
    echo "CREATE DATABASE ${DB_NAME} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql -u${DB_USER} -p${DB_PASS}

    # default db
    python ../manage.py syncdb --noinput
    python ../manage.py migrate

    # echo 'master data'
    # mysql -u${DB_USER} -p${DB_PASS} ${DB_NAME} < ./master_data.sql

    # echo 'debug data'
    # mysql -u${DB_USER} -p${DB_PASS} ${DB_NAME} < ./debug_data.sql

fi

