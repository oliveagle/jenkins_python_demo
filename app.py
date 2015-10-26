#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 oliveagle <oliveagle@gmail.com>
#
# Distributed under terms of the MIT license.
#
# File:  hello.py
# Date:  2015-10-26 15:41

"""

"""
from flask import Flask, send_file
from apis_v2.views import apis_v2
from apis_v1.views import apis_v1

app = Flask(__name__, 
            static_url_path='/cover', 
            static_folder='cover')


@app.route("/")
def index():
    return send_file("index.html")

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/hello_raise")
def hello_raise():
    raise NotImplementedError

@app.route("/v1/api")
def api_v1():
    """
    this will return a list os int
    """
    return [int(x) for x in xrange(0,100)]


@app.route('/cover/<path:path>')
def coverage_report(path):
    print path
    return send_from_directory('cover', path)

app.register_blueprint(apis_v2, url_prefix="/apis/v2")
app.register_blueprint(apis_v1, url_prefix="/apis/v1")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

