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

from mock import MagicMock, patch

_page_num = views.page_num
_page = views.page

class TestCaseViewsPage(unittest.TestCase):

    def setUp(self):
        views.page_num = _page_num
        views.page = _page

    def test_mock_page_num(self):
        # _page_num = views.page_num
        views.page_num = MagicMock(return_value=8888)
        self.assertEqual(views.page_num(1), 8888)
        # views.page_num = _page_num

    def test_page_num(self):
        self.assertEqual(views.page_num(1), 1)
        self.assertEqual(views.page_num(3), 3)

    def test_page(self):
        self.assertEqual(views.page(1), "/apis/v2/page/1")

        views.page = MagicMock(return_value="/apis/v1/page/1")
        self.assertEqual(views.page(1), "/apis/v2/page/1")    # fails

    @patch("apis_v2.views.page_num")
    def test_mock_patch(self, mock_page_num):
        mock_page_num.return_value = 500
        self.assertEqual(mock_page_num(12), 500)
