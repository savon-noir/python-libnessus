#!/usr/bin/env python

#from libnessus.objects import NessusReport
from libnessus.objects import NessusHost
from test_nessus import TestNessus


class TestNessusReport(TestNessus):
    """Test Report object"""

    def test_hosts(self):
        """ Check that all obj in this array are NessusHost
            Check the number of host in a report
            Check the attribute is an array
        """
        for testfile in self.flist:
            self.assertEqual(len(testfile['report'].hosts), testfile['hosts'])
            self.assertEqual(
                isinstance(testfile['report'].hosts, (
                    list, tuple)), True)
            for host in testfile['report'].hosts:
                self.assertEqual(
                    isinstance(host, NessusHost), True)

    def test_save(self):
        """"""
    def test_diff(self):
        """"""
    def test_started(self):
        """"""
    def test_commandline(self):
        """"""
    def test_version(self):
        """"""
    def test_scan_type(self):
        """"""
    def test_get_host_byid(self):
        """"""
    def test_endtime(self):
        """"""
    def test_summary(self):
        """"""
    def test_elapsed(self):
        """"""
    def test_hosts_up(self):
        """"""
    def test_hosts_down(self):
        """"""
    def test_hosts_total(self):
        """"""
    def test_get_raw_data(self):
        """"""
