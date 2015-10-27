#! /bin/bash
#
# bootstrap.sh
# Copyright (C) 2015 oliveagle <oliveagle@gmail.com>
#
# Distributed under terms of the MIT license.
#


if [ ! -d .venv ]; then
  virtualenv --no-site-packages .venv
fi

#source .venv/bin/activate && \
#  pip install distribute pbr && \
#  pip install -r requirements.txt

# already download packages from internet. 
OPTS="--no-index --find-links=../python_packages -U"
soruce .venv/bin/activate && \
  pip install $OPTS setuptools distribute pbr && \
  pip install $OPTS -r requirements.txt
