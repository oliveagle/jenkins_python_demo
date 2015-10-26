#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 oliveagle <oliveagle@gmail.com>
#
# Distributed under terms of the MIT license.
#
# File:  test_hello.py
# Date:  2015-10-26 15:59

"""

"""

import unittest
from app import hello, hello_raise
from app import api_v1
import logging

class ViewTestCaseHello(unittest.TestCase):

    def test_hello_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            hello_raise()

    def test_hello(self):
        res = hello()
        if res != "Hello World!":
            raise NotImplementedError

    def test_api_v1(self):
        res = api_v1()
        logging.error(res)
        self.assertTrue(len(res)>0)

