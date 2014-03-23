#!/usr/bin/env python

#from libnessus.objects import NessusHost
from test_nessus import TestNessus


class TestHost(TestNessus):
    """Test Host object"""

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
        """test_started :useless already tested in test_ip"""

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

    def test_get_host_properties(self):
        """"""

    def test_get_host_property(self):
        """"""
