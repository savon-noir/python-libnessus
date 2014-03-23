#!/usr/bin/env python

from libnessus.objects import NessusHost
from test_nessus import TestNessus
from datetime import datetime


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
        """Test the startime of the scan"""
        for testfile in self.flist:
            rep_start = testfile['report'].started
            datefromrep = datetime.strptime(testfile['rep_start'],
                                            '%a %b %d %H:%M:%S %Y')
            self.assertEqual(rep_start, datefromrep)

#    def test_commandline(self):
#        """"""
#    def test_version(self):
#        """"""
#    def test_scan_type(self):
#        """"""
#    def test_get_host_byid(self):
#        """"""
    def test_endtime(self):
        """Test the endtime of the scan"""
        for testfile in self.flist:
            rep_end = testfile['report'].endtime
            expected = datetime.strptime(testfile['rep_end'],
                                         '%a %b %d %H:%M:%S %Y')
            err_msg = "In file %s expected : %s value : %s " % (testfile['file'],
                                                                expected,
                                                                rep_end)
            self.assertEqual(rep_end, expected, err_msg)

    def test_summary(self):
        """"""
    def test_elapsed(self):
        """test the difference between end and start time"""
        for testfile in self.flist:
            value = testfile['report'].endtime - testfile['report'].started
            end = datetime.strptime(testfile['rep_end'], '%a %b %d %H:%M:%S %Y')
            start = datetime.strptime(testfile['rep_start'], '%a %b %d %H:%M:%S %Y')
            expected = end - start
            err_msg = "In file %s expected : %s value : %s " % (testfile['file'],
                                                                expected,
                                                                value)
            self.assertEqual(value, expected, err_msg)

#Remove the following -->Useless
#    def test_hosts_up(self):
#        """"""
#    def test_hosts_down(self):
#        """"""
    def test_hosts_total(self):
        """Return the number of host in the report"""
        for testfile in self.flist:
            value = testfile['report'].hosts_total
            expected = testfile['hosts']
            err_msg = "In file %s expected : %s value : %s " % (testfile['file'],
                                                                expected,
                                                                value)
            self.assertEqual(value, expected, err_msg)

#    def test_get_raw_data(self):
#        """"""
