#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 oliveagle <oliveagle@gmail.com>
#
# Distributed under terms of the MIT license.
#
# File:  views.py
# Date:  2015-10-26 16:46

"""

"""
from flask import Blueprint

apis_v1 = Blueprint('apis_v1', __name__)

@apis_v1.route('/page', defaults={'page': 'index'})
@apis_v1.route('/page/<page>')
def page(page):
    return "/apis/v1/page/%s" % (page)


@apis_v1.route('/page_num', defaults={'page': 'index'})
@apis_v1.route('/page_num/<page>')
def page_num(page):
    return page

