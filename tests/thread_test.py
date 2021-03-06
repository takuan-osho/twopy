# -*- coding: utf-8 -*-

import os
import unittest
import datetime
from twopy.thread import make_dat_url, make_thread_url, \
                         make_title_from_dat, Thread


class TestThreadModule(unittest.TestCase):
    def setUp(self):
        dat_filepath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "data", "stema.dat")
        fp = file(dat_filepath, "r")
        self.dat_string = unicode(fp.read(), "Shift-JIS", "ignore")

    def test_make_thread_url(self):
        result = make_thread_url("http://engawa.2ch.net/news/", "1234.dat")
        self.assertEqual(
            result,
            "http://engawa.2ch.net/test/read.cgi/news/1234/")
        result = make_thread_url("http://engawa.2ch.net/news", "456789.dat")
        self.assertEqual(
            result,
            "http://engawa.2ch.net/test/read.cgi/news/456789/")

    def test_make_dat_url(self):
        result = make_dat_url("http://engawa.2ch.net/news/", "1234.dat")
        self.assertEqual(result, "http://engawa.2ch.net/news/dat/1234.dat")
        result = make_dat_url("http://engawa.2ch.net/news", "456789.dat")
        self.assertEqual(result, "http://engawa.2ch.net/news/dat/456789.dat")

    def test_make_title_from_dat(self):
        result = make_title_from_dat(self.dat_string)
        self.assertEqual(result, u"ステマと言われて困っています。- ２ちゃんねる知恵袋")

    def test_Thread(self):
        t = Thread(self.dat_string)
        self.assertEqual(len(t), 10)
        self.assertEqual(len([a for a in t]), 10)
        self.assertEqual(len(t[1:10]), 10)
        self.assertEqual(t.title, u"ステマと言われて困っています。- ２ちゃんねる知恵袋")
        self.assertTrue(isinstance(t.comments, list))
        self.assertTrue(isinstance(t.last_retrieved, datetime.datetime))
