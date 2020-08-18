#!/usr/bin/python3
""" Make a .tgz archive from the contents of the web_static """
from fabric.operations import local
from datetime import datetime


def do_pack():
    local('mkdir -p versions')
    local('tar -czvf versions/web_static_\
{}.tgz web_static'.format(datetime.strftime(datetime.now(), "%Y%m%d%H%M")))
