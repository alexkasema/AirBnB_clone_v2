#!/usr/bin/python3

""" Deploy the archive! """

from fabric.api import env, run, local, put
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
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/{}'.format(archive.strip('.tgz'))
        symb_link = '/data/web_static/current'

        put(archive, '/tmp/')
        run('sudo mkdir -p {}/'.format(path))
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('sudo rm /tmp/{}'.format(archive))
        run('sudo mv {}/web_static/* {}'.format(path, path))
        run('sudo rm -rf {}/web_static'.format(path))
        run('sudo rm -rf {}'.format(symb_link))
        run('sudo ln -s {} {}'.format(path, symb_link))
        print('New version deployed!')
        return True
    except:
        return False


