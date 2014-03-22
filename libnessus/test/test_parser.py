#!/usr/bin/env python

from libnessus.parser import NessusParser
from libnessus.objects import NessusReport
from test_nessus import TestNessus
from libnessus.objects import NessusReport, NessusHost, NessusVuln
from test_nessus import TestNessus
import xml.etree.ElementTree as ET


class TestParser(TestNessus):
    """Unit test of parser"""
    def test_return_class(self):
        """test_return_class : Check the returned object is NessusReport"""
        for testfile in self.flist:
            self.assertEqual(isinstance(testfile['report'],
                             NessusReport), True)

    def test_number_of_host_in_report(self):
        """test_number_of_host_in_report :
            Check the number of host in the repport"""
        for testfile in self.flist:
            self.assertEqual(len(testfile['report'].hosts), testfile['hosts'])

    def test_badfile_for_excepetion(self):
        """test_badfile_for_excepetion :
            Check to raise when wrong input file"""
        for testfile in self.badlist:
            fd = open(testfile['file'], 'r')
            s = fd.read()
            fd.close()
            self.assertRaises(Exception, NessusParser.parse, s)

    def test_parse_host(self):
        """test_parse_host : check host parsing"""

    def test_parse_vulnerability(self):
        """test_parse_vulnerability : check vuln parsing"""
        fd = open("%s/files/hostnessus.xml" % self.fdir, 'r')
        s = fd.read()
        fd.close()
        root = ET.fromstring(s)
        host = NessusParser.parse_host(root=root)
        self.assertEqual(
                          isinstance(host, NessusHost), True)

    def test_parse_vulnerability(self):
        """test_parse_vulnerability : check vuln parsing"""
        fd = open("%s/files/reportitems.xml" % self.fdir, 'r')
        s = fd.read()
        fd.close()
        root = ET.fromstring(s)
        report_item = NessusParser.parse_vulnerability(root)
        self.assertEqual(isinstance(report_item, NessusVuln), True)
