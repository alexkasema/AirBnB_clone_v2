#!/usr/bin/python3

""" Compress before sending """

from fabric.api import env, local
from datetime import datetime


env.user = 'ubuntu'
env.hosts = [
    '100.26.223.120',
    '100.26.18.64'
]


def do_pack():
    """ generates a .tgz archive from the contents of the web_static folder
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("sudo mkdir -p ./versions")
    my_archive = "./versions/web_static_{}".format(now)
    local("sudo tar -czvf {}.tgz web_static".format(my_archive))
    created_archive = "{}.tgz".format(my_archive)

    if created_archive:
        return created_archive
    else:
        None
