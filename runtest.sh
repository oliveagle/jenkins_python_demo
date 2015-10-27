#! /bin/bash
#
# runtest.sh
# Copyright (C) 2015 oliveagle <oliveagle@gmail.com>
#
# Distributed under terms of the MIT license.
#

if [ -d .venv ]; then
  . .venv/bin/activate
fi

if [ ! -d cover ];then
	mkdir cover
fi
nosetests -vv \
	--with-coverage --cover-html \
	--cover-package=app,apis_v1,apis_v2 \
	--with-html --html-file=./cover/test_result.html \
  --with-xunit --xunit-file=./cover/xunit.xml
