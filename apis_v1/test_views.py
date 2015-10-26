#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 oliveagle <oliveagle@gmail.com>
#
# Distributed under terms of the MIT license.
#
# File:  test_views.py
# Date:  2015-10-26 16:57

"""

"""
import unittest

import views


class TestCaseViewsPage(unittest.TestCase):

    def test_page_num(self):
        self.assertEqual(views.page_num(1), 1)
        self.assertEqual(views.page_num(3), 3)

    def test_page(self):
        res = views.page(1)
        self.assertEqual(res, "/apis/v2/page/1")    # fail

