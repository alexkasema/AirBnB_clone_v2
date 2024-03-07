#!/usr/bin/python3

""" Full deployment to servers """

from fabric.api import env, run, local, put

from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['100.26.18.64', '100.26.223.120']


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

        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(symb_link))
        run('ln -s {} {}'.format(path, symb_link))
        print('New version deployed!')
        return True
    except Exception:
        return False


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    isSuccess = do_deploy(archive_path)
    return isSuccess


def do_clean(number=0):
    """
    deletes out-of-date archives
    """
    if number == 0 or number == 1:
        with lcd('./versions/'):
            local("ls -lv | rev | cut -f 1 | rev | \
            head -n +1 | xargs -d '\n' rm -rf")
        with cd('/data/web_static/releases/'):
            run("sudo ls -lv | rev | cut -f 1 | \
            rev | head -n +1 | xargs -d '\n' rm -rf")
    else:
        with lcd('./versions/'):
            local("ls -lv | rev | cut -f 1 | rev | \
            head -n +{} | xargs -d '\n' rm -rf".format(number))
        with cd('/data/web_static/releases/'):
            run("sudo ls -lv | rev | cut -f 1 | \
            rev | head -n +{} | xargs -d '\n' rm -rf".format(number))
