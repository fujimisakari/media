# -*- coding: utf-8 -*-

from fabric.api import env, run, sudo
from fabric.context_managers import cd
from fabric.contrib.files import exists


env.hosts = ['www6096uf.sakura.ne.jp']
env.DEPLOY_DIR = '/var/www/'


def graceful():
    sudo('apache2ctl graceful')


def importcsv():
    with cd(env.DEPLOY_DIR):
        with cd('media'):
            run('./manage.py importcsv')
            sudo('/etc/init.d/memcached restart')


def exportcsv():
    with cd(env.DEPLOY_DIR):
        with cd('media'):
            run('sudo -u www-data ./manage.py exportcsv')


def migrate():
    with cd(env.DEPLOY_DIR):
        with cd('media'):
            run('./manage.py migrate top')
            run('./manage.py migrate book')


def deploy():
    with cd(env.DEPLOY_DIR):
        if not exists('media'):
            run('sudo -u www-data git clone git@github.com:fujimisakari/media.git')

        with cd('media'):
            run('sudo -u www-data git pull')
            sudo('apache2ctl graceful')
