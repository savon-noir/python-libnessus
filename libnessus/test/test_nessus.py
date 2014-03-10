#!/usr/bin/env python

import unittest
import os
from libnessus.parser import NessusParser


class TestNessus(unittest.TestCase):
    '''TestNEssus class only contains the setUp functions all test class will
       inherit from this one'''
    def setUp(self):
        '''setup a table of report based on the files in flist '''
        self.fdir = os.path.dirname(os.path.realpath(__file__))
        self.flist = [
            {'file': "%s/%s" % (self.fdir, 'files/nessus_report_local2.nessus'),
             'hosts': 1},
            {'file': "%s/%s" % (self.fdir, 'files/nessus_report_localpci.nessus'),
             'hosts': 1},
            {'file': "%s/%s" % (self.fdir, 'files/nessus_report_test_local.nessus'),
             'hosts': 2},
        ]
        #parse them once and for all
        for testfile in self.flist:
            fd = open(testfile['file'], 'r')
            s = fd.read()
            fd.close()
            nrp = NessusParser.parse(s)
            testfile['report'] = nrp
        #cannot parse these file as it will provoque an excepetion
        self.badlist = [
            {'file': "%s/%s" % (self.fdir, 'files/xxxxxxxx.nessus'),
             'hosts': 0},
        ]
