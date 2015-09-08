FROM debian:8
ENV DEBIAN_FRONTEND noniteractive

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["dpkg-buildpackage", "-us", "-uc"]

RUN apt-get -qq update && apt-get -qq -y --no-install-recommends install \
    automake \
    autoconf \
    build-essential \
    cmake \
    debhelper \
    dh-virtualenv \
    devscripts \
    python-dev \
    python-setuptools

RUN easy_install pip

COPY docker-entrypoint.sh /
