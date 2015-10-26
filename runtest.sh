#! /bin/bash
#
# runtest.sh
# Copyright (C) 2015 oliveagle <oliveagle@gmail.com>
#
# Distributed under terms of the MIT license.
#

if [ ! -d cover ];then
	mkdir cover
fi
nosetests -vv \
	--with-coverage --cover-html \
	--cover-package=app,apis_v1,apis_v2 \
	--with-html --html-file=./cover/test_result.html \
	2>&1 | tee cover/test.log


