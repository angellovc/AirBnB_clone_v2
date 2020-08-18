#!/usr/bin/python3
"""  Fabric script that distributes an archive to your web servers """
from fabric.api import *
from os.path import exists
env.hosts = ['35.231.105.155', '34.75.216.134']


def do_deploy(archive_path):
    """ deploy web_static version on web-01 and web-02 """
    if exists(archive_path):
        print(archive_path)
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        folder_name = file_name[-1].replace('.tgz', '')
        run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
            file_name,
            folder_name
        ))
        run('rm /tmp/{}'.format(file_name))
        run('mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}'.format(folder_name, folder_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            folder_name
            ))
        run('rm -rf /data/web_static/current')
        run('ln -s \
/data/web_static/releases/{}/ /data/web_static/current'.format(folder_name))
        return True
    else:
        return False
