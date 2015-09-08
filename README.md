# Debian `dpkg-buildpackage` for Docker

This software consists of two parts:

1. A base Docker image `klokantech/dpkg-buildpackage` built
   automatically by Docker Hub from the `Dockerfile` in this
   repository.

2. A Python package `dpkg_buildpackage` that wraps a command
   line interface around the Docker image.


## Installation

```shell
$ pip install -e \
git+https://github.com/klokan/dpkg-buildpackage.git@master#egg=dpkg-buildpackage
```


## Usage

```shell
$ dpkg-buildpackage-docker .../src
```

The source directory must be properly debianized, ie. it must
contain a valid `debian` subdirectory. The resulting `.deb`
package will be placed in the same directory.

The base image contains essential packages for building software,
including Python. If extra tools are needed, you can specify
a custom `debian/Dockerfile` file and it will be automatically
built and used to generate the package. There are some restrictions
it must adhere to.

1. It must descend from the `klokantech/dpkg-buildpackage` base image.

2. It must not modify `ENTRYPOINT` or `CMD`.
