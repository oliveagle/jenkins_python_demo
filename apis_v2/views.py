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
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

apis_v2 = Blueprint('apis_v2', __name__)

@apis_v2.route('/page', defaults={'page': 'index'})
@apis_v2.route('/page/<page>')
def page(page):
    return "/apis/v2/page/%s" % (page)


@apis_v2.route('/page_num', defaults={'page': 'index'})
@apis_v2.route('/page_num/<page>')
def page_num(page):
    return page