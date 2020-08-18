#!/usr/bin/python3
"""  Fabric script that distributes an archive to your web servers """
from fabric.api import *
from fabric.operations import local
from os.path import exists
from datetime import datetime


env.hosts = ['35.231.105.155', '34.75.216.134']


def deploy():
    """ creates and distributes an archive to web servers """
    result = do_pack()
    if result is None:
        return False
    else:
        file_name = result.__dict__['command']
        file_name = file_name.split(' ')[-2]
        return do_deploy(file_name)


def do_deploy(archive_path):
    """ deploy web_static version on web-01 and web-02 """
    if exists(archive_path):
        print(archive_path)
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        folder_name = file_name.replace('.tgz', '')
        print(folder_name)
        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
            file_name,
            folder_name
        ))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/{}/web_static/* /data/web_static/releases/{}'.format(
            '/data/web_static/releases',
            folder_name,
            folder_name
            ))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            folder_name
            ))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/{}/ /data/web_static/current'.format(
            '/data/web_static/releases',
            folder_name
            ))
        return True
    else:
        return False


def do_pack():
    """ add all files in the folder web_static to the final archive """
    local('mkdir -p versions')
    result = local('tar -czvf versions/web_static_\
{}.tgz web_static'.format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    if result.failed:
        return None
    else:
        return result
