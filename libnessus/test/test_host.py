#!/usr/bin/env python

from libnessus.objects.reporthost import NessusReportHost
from .test_nessus import TestNessus
import copy


class TestHost(TestNessus):
    """Test Host object"""

    def test_init(self):
        """test exception with incomplete obj"""
        rep = self.flist[0]
        hosts = rep['report'].hosts
        host = hosts[0]
        host_properties = host.get_host_properties
        report_items = host.get_report_items
        del host_properties['name']
        self.assertRaises(Exception, NessusReportHost, host_properties, report_items)

    def test_name(self):
        """check the name of hosts"""
        for sample in self.flist:
            list_hosts = sample['report'].hosts
            i = 0
            for value in list_hosts:
                expected = sample['hosts_names'][i]
                err_msg = "In file %s expected : %s value : %s " % (sample['file'],
                                                                    expected,
                                                                    value)
                self.assertEqual(value.name, expected, err_msg)
                i = i + 1

    def test_ip(self):
        """check the ip of hosts"""
        for sample in self.flist:
            list_hosts = sample['report'].hosts
            i = 0
            for value in list_hosts:
                expected = sample['hosts_ip'][i]
                err_msg = "In file %s expected : %s value : %s " % (sample['file'],
                                                                    expected,
                                                                    value)
                self.assertEqual(value.ip, expected, err_msg)
                i = i + 1

    def test_address(self):
        """test_address :useless already tested in test_ip"""

    def test_started(self):
        """Check scan start time"""
        for sample in self.flist:
            list_hosts = sample['report'].hosts
            i = 0
            for value in list_hosts:
                expected = sample['hosts_start'][i]
                err_msg = "In file %s expected : %s value : %s " % (sample['file'],
                                                                    expected,
                                                                    value)
                self.assertEqual(value.started, expected, err_msg)
                i = i + 1

    def test_ended(self):
        """Check scan end time"""
        for sample in self.flist:
            list_hosts = sample['report'].hosts
            i = 0
            for value in list_hosts:
                expected = sample['hosts_end'][i]
                err_msg = "In file %s expected : %s value : %s " % (sample['file'],
                                                                    expected,
                                                                    value)
                self.assertEqual(value.ended, expected, err_msg)
                i = i + 1

    def test_get_summary_total_cves(self):
        """Test the total number of CVE for the host"""
        for sample in self.flist:
            list_hosts = sample['report'].hosts
            i = 0
            for value in list_hosts:
                expected = sample['patch-summary-total-cves'][i]
                err_msg = "In file %s expected : %s value : %s " % (sample['file'],
                                                                    expected,
                                                                    value)
                self.assertEqual(value.get_summary_total_cves, expected, err_msg)
                i = i + 1

    def test_get_host_properties(self):
        """test the number of properties >=4"""
        for sample in self.flist:
            list_hosts = sample['report'].hosts
            for value in list_hosts:
                expected = ">=4"
                err_msg = "In file %s expected : %s value : %s " % (sample['file'],
                                                                    expected,
                                                                    value)

                self.assertNotEqual(len(value.get_host_properties), 0, err_msg)
                self.assertNotEqual(len(value.get_host_properties), 1, err_msg)
                self.assertNotEqual(len(value.get_host_properties), 2, err_msg)
                self.assertNotEqual(len(value.get_host_properties), 3, err_msg)

    def test_get_host_property(self):
        """Check getHostproperty with a key as param + None value"""
        rep = self.flist[0]
        hosts = rep['report'].hosts
        value = hosts[0]
        expected = "localhost"

        err_msg = "Expected : %s value : %s " % (
                                                            expected,
                                                            value)
        self.assertEqual(value.get_host_property("name"), expected, err_msg)
        err_msg = "Expected : %s value : %s " % (
                                                            "None",
                                                            value)
        self.assertEqual(value.get_host_property("kjskljdsfjname"), None, err_msg)

    def test_get_total_vuln(self):
        """Test the total number of ReportItem in a host"""
        for sample in self.flist:
            list_hosts = sample['report'].hosts
            i = 0
            for value in list_hosts:
                expected = sample['totalVulnPerHost'][i]
                err_msg = "In file %s expected : %s value : %s " % (sample['file'],
                                                                    expected,
                                                                    value.get_total_vuln)
                self.assertEqual(value.get_total_vuln, expected, err_msg)
                i = i + 1

    def test_get_hostprop_attr(self):
        """test return a set of key properties"""
        for sample in self.flist:
            list_hosts = sample['report'].hosts
            for value in list_hosts:
                expected = True
                value = value.get_hostprop_attr
                value = isinstance(value, set)
                self.assertEqual(value, expected)

    def test_hash(self):
        """check hash function"""
        expected = 1
        for sample in self.flist:
            list_hosts = sample['report'].hosts
            i = 0
            for value in list_hosts:
                a = set()
                a.add(value)
                a.add(value)
                self.assertEqual(len(a), expected)
                i = i + 1

    def test_iscomparable(self):
        """
        test_host: test to throw TypeError in case of uncompatible obj
        """
        dictHost = {
            'host-ip': "255.255.255.255",
            'name': "wakawakawaka",
            'HOST_START': "hh:mm",
            'HOST_END': "HH:MM",
            }
        forged = NessusReportHost(dictHost)
        for sample in self.flist:
            list_hosts = sample['report'].hosts
            for value in list_hosts:
                self.assertRaises(TypeError, value.iscomparable, forged)
        # test different type
        self.assertRaises(TypeError, value.iscomparable, 5)

    def test_eq(self):
        """
        test_host : test equality
        retrieve self.forgedHost and play with it
        no need to test with other ip since allready tested in iscomparable
        """
        h1 = self.forgedHost
        h2 = copy.deepcopy(h1)
        # after copy should be equal
        self.assertEqual((h1 == h2), True)
        # force another name should return false
        h2.__dict__['_NessusReportHost__host_properties']['name'] = 'wakawaka'
        self.assertEqual((h1 == h2), False)
        # check the exception from iscomparable is reraised
        self.assertRaises(TypeError, h1.__eq__, 5)

    def test_ne(self):
        """
        test_host : test not equal
        retrieve self.forgedHost and play with it
        no need to test with other ip since already tested in iscomparable
        """
        h1 = self.forgedHost
        h2 = copy.deepcopy(h1)
        # after copy should be equal
        self.assertEqual((h1 != h2), False)
        # force another name should return True
        h2.__dict__['_NessusReportHost__host_properties']['name'] = 'wakawaka'
        self.assertEqual((h1 != h2), True)
        # check the exception from iscomparable is reraised
        self.assertRaises(TypeError, h1.__ne__, 5)
