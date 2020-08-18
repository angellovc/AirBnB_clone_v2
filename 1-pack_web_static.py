#!/usr/bin/python3
""" Make a .tgz archive from the contents of the web_static """
from fabric.operations import local
from datetime import datetime


def do_pack():
    """ add all files in the folder web_static to the final archive """
    local('mkdir -p versions')
    result = local('tar -czvf versions/web_static_\
{}.tgz web_static'.format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    if result.failed:
        return None
    else:
        return result
