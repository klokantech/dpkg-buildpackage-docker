import argparse
import os.path
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('src', help='debianized directory')
    parser.add_argument('dst', help='output directory')
    parser.add_argument(
        'extra_args',
        nargs=argparse.REMAINDER,
        help='extra arguments for dpkg-buildpackage')
    args = parser.parse_args()
    build(args.src, args.dst, args.extra_args)


def build(src, dst, extra_args=None):
    """Build a package."""
    if extra_args is None:
        extra_args = []
    src = realpath(src)
    dst = realpath(dst)
    dockerfile_path = os.path.join(src, 'debian', 'Dockerfile')
    if os.path.exists(dockerfile_path):
        image = 'dpkg-buildpackage/' + os.path.basename(src)
        with open(dockerfile_path, 'rb') as dockerfile:
            docker(['build', '-q', '-t', image, '-'], dockerfile.read())
    else:
        image = 'klokantech/dpkg-buildpackage'
    args = [
        'run', '--rm',
        '-v', '{}/:/mnt/src/'.format(src),
        '-v', '{}/:/mnt/dst/'.format(dst),
        '-v', '/var/cache/pip/:/var/cache/pip/',
        image,
    ]
    if extra_args:
        args.append('dpkg-buildpackage')
        args.extend(extra_args)
    docker(args)


def docker(args, input_=None):
    """Call the Docker Engine executable."""
    run_command(['/usr/bin/docker'] + args, input_)


def run_command(cmd, input_=None):
    """Execute command and check for success."""
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    _out, err = proc.communicate(input_)
    if proc.returncode != 0:
        raise Exception(err)


def realpath(path):
    return os.path.abspath(os.path.expanduser(path))


if __name__ == '__main__':
    main()