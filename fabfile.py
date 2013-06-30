# -*- coding: utf-8 -*-

from fabric.api import env, run, sudo
from fabric.context_managers import cd
from fabric.contrib.files import exists


env.hosts = ['www6096uf.sakura.ne.jp']
env.DEPLOY_DIR = '/var/www/'


def graceful():
    sudo('sudo apache2ctl graceful')


def deploy():

    with cd(env.DEPLOY_DIR):
        if not exists('media'):
            run('git clone git@github.com:fujimisakari/media.git')

        with cd('media'):
            run('git pull')
            run('git pull origin master')
