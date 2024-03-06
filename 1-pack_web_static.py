#!/usr/bin/python3

""" Compress before sending """

from fabric.api import local
from datetime import datetime


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
        return None
