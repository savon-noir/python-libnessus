#!/usr/bin/env python

from libnessus.objects.reporthost import NessusReportHost
from .test_nessus import TestNessus
from datetime import datetime
import copy

class TestNessusReport(TestNessus):
    """Test Report object"""

    def test_hosts(self):
        """ Check that all obj in this array are NessusReportHost
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
                    isinstance(host, NessusReportHost), True)

    def test_save(self):
        """Test the save method...
           This is done in the plugin test
        """

    def test_iscomparable(self):
        """
        test_iscomparable test to throm typeError if not the same type
        """
        value = self.forgedreport
        # test different type
        self.assertRaises(TypeError, value.iscomparable, 5)

    def test_eq(self):
        """"""
        value = self.forgedreport
        # test different type
        self.assertRaises(TypeError, value.__eq__, 5)
        value2 = copy.deepcopy(value)
        self.assertEqual((value == value2), True)

    def test_ne(self):
        """"""
        value = self.forgedreport
        # test different type
        self.assertRaises(TypeError, value.__eq__, "5")
        value2 = copy.deepcopy(value)
        self.assertEqual((value != value2), False)

    def test_started(self):
        """Test the startime of the scan"""
        for testfile in self.flist:
            rep_start = testfile['report'].started
            datefromrep = datetime.strptime(testfile['rep_start'],
                                            '%a %b %d %H:%M:%S %Y')
            self.assertEqual(rep_start, datefromrep)

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

    def test_hosts_total(self):
        """Return the number of host in the report"""
        for testfile in self.flist:
            value = testfile['report'].hosts_total
            expected = testfile['hosts']
            err_msg = "In file %s expected : %s value : %s " % (testfile['file'],
                                                                expected,
                                                                value)
            self.assertEqual(value, expected, err_msg)
