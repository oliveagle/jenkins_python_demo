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

source .venv/bin/activate && \
  pip install distribute pbr && \
  pip install -r requirements.txt
