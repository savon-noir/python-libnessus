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
             'hosts': 1,
             'rep_start': "Fri Oct  4 15:06:24 2013",
             'rep_end': "Fri Oct  4 15:07:30 2013", },
            {'file': "%s/%s" % (self.fdir, 'files/nessus_report_localpci.nessus'),
             'hosts': 1,
             'rep_start': "Tue Jan  7 08:19:20 2014",
             'rep_end': "Tue Jan  7 08:19:25 2014", },
            {'file': "%s/%s" % (self.fdir, 'files/nessus_report_test_local.nessus'),
             'hosts': 2,
             'rep_start': "Tue Oct  1 18:19:31 2013",
             'rep_end': "Wed Oct  2 09:03:58 2013", },
            {'file': "%s/%s" % (self.fdir, 'files/nessus_report_local_3.nessus'),
             'hosts': 3,
             'rep_start': "Thu Mar 20 00:30:57 2014",
             'rep_end': "Thu Mar 20 01:22:17 2014", },
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
