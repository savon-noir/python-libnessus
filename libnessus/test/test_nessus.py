#!/usr/bin/env python

import unittest
import os
from libnessus.parser import NessusParser
from libnessus.objects import NessusHost, NessusVuln, NessusReport

class TestNessus(unittest.TestCase):
    '''TestNEssus class only contains the setUp functions all test class will
       inherit from this one'''
    def setUp(self):
        '''setup a table of report based on the files in flist '''
        fdir = os.path.dirname(os.path.realpath(__file__))
        self.flist = [
            {'file': "%s/%s" % (fdir, 'files/nessus_report_local2.nessus'),
             'hosts': 1},
            {'file': "%s/%s" % (fdir, 'files/nessus_report_localpci.nessus'),
             'hosts': 1},
            {'file': "%s/%s" % (fdir, 'files/nessus_report_test_local.nessus'),
             'hosts': 2},
        ]
        """
            nessus_report_local2.nessus:<ReportHost name="localhost"><HostProperties>
            nessus_report_localpci.nessus:<ReportHost name="127.0.0.1"><HostProperties>
            nessus_report_test_local.nessus:<ReportHost name="192.168.1.3"><HostProperties>
            nessus_report_test_local.nessus:<ReportHost name="192.168.1.1"><HostProperties>
        """
        self.badlist = [
            {'file': "%s/%s" % (fdir, 'files/xxxxxxxx.nessus'),
             'hosts': 0},
        ]

    def test_class_parser(self):
        for testfile in self.flist:
            fd = open(testfile['file'], 'r')
            s = fd.read()
            fd.close()
            nrp = NessusParser.parse(s)
            self.assertEqual(isinstance(nrp, NessusReport), True)
        for testfile in self.badlist:
            fd = open(testfile['file'], 'r')
            s = fd.read()
            fd.close()
            self.assertRaises(Exception,NessusParser.parse,s)
