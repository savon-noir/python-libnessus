#!/usr/bin/env python

from test_nessus import TestNessus
from libnessus.objects.reportitem import NessusReportItem


class TestVuln(TestNessus):
    """Unit test of vuln object"""
    def test_port(self):
        """test the port return"""
        i = 0
        for vuln in self.VulnList:
            value = vuln.port
            expected = self.expected_vuln[i]['port']
            self.assertEqual(value, expected)
            i = i + 1

    def test_service(self):
        """test the service name"""
        i = 0
        for vuln in self.VulnList:
            value = vuln.service
            expected = self.expected_vuln[i]['svc_name']
            self.assertEqual(value, expected)
            i = i + 1

    def test_protocol(self):
        """test the protocol"""
        i = 0
        for vuln in self.VulnList:
            value = vuln.protocol
            expected = self.expected_vuln[i]['protocol']
            self.assertEqual(value, expected)
            i = i + 1

    def test_severity(self):
        """test severity"""
        i = 0
        for vuln in self.VulnList:
            value = vuln.severity
            expected = self.expected_vuln[i]['severity']
            self.assertEqual(value, expected)
            i = i + 1

    def test_plugin_id(self):
        """test plugin id"""
        i = 0
        for vuln in self.VulnList:
            value = vuln.plugin_id
            expected = self.expected_vuln[i]['plugin_id']
            self.assertEqual(value, expected)
            i = i + 1

    def test_plugin_name(self):
        """test plugin name"""
        i = 0
        for vuln in self.VulnList:
            value = vuln.plugin_name
            expected = self.expected_vuln[i]['plugin_name']
            self.assertEqual(value, expected)
            i = i + 1

    def test_plugin_family(self):
        """test plugin family"""
        i = 0
        for vuln in self.VulnList:
            value = vuln.plugin_family
            expected = self.expected_vuln[i]['plugin_family']
            self.assertEqual(value, expected)
            i = i + 1

    def test_get_vuln_info(self):
        """test return type of vuln_info"""
        i = 0
        for vuln in self.VulnList:
            value = isinstance(vuln.get_vuln_info, dict)
            expected = True
            self.assertEqual(value, expected)
            i = i + 1

    def test_get_vuln_risk(self):
        """test return type of risk factor"""
        i = 0
        for vuln in self.VulnList:
            value = isinstance(vuln.get_vuln_risk, dict)
            expected = True
            self.assertEqual(value, expected)
            i = i + 1

    def test_get_vuln_plugin(self):
        """
        test return type of plugin dict
        """
        i = 0
        for vuln in self.VulnList:
            value = isinstance(vuln.get_vuln_plugin, dict)
            expected = True
            self.assertEqual(value, expected)
            i = i + 1

    def test_get_vuln_xref(self):
        """test return type of xref"""
        i = 0
        for vuln in self.VulnList:
            value = isinstance(vuln.get_vuln_xref, dict)
            expected = True
            self.assertEqual(value, expected)
            i = i + 1

    def test_synopsis(self):
        """test synopsis"""
        i = 0
        for vuln in self.VulnList:
            value = vuln.synopsis
            expected = self.expected_vuln[i]['synopsis']
            self.assertEqual(value, expected)
            i = i + 1

    def test_description(self):
        """test return type od descr"""
        i = 0
        for vuln in self.VulnList:
            value = isinstance(vuln.description, str)
            expected = True
            self.assertEqual(value, expected)
            i = i + 1

    def test_solution(self):
        """test solution string"""
        i = 0
        for vuln in self.VulnList:
            value = vuln.solution
            expected = self.expected_vuln[i]['solution']
            self.assertEqual(value, expected)
            i = i + 1

    def test_eq(self):
        """test the equal method"""
        """
           compare all reportitem to themself to check equality
        """
        for vuln in self.VulnList:
            value = NessusReportItem(vuln.get_vuln_info.copy())
            expected = NessusReportItem(vuln.get_vuln_info.copy())
            self.assertEqual(value, expected)
        # test different type
        self.assertRaises(TypeError, value.__eq__, 5)

    def test_ne(self):
        """test the not equal operator"""
        for vuln in self.VulnList:
            forgeditem = vuln.get_vuln_info.copy()
            forgeditem['plugin_name'] = "FORGED"
            value = NessusReportItem(forgeditem)
            expected = NessusReportItem(vuln.get_vuln_info)
            value = value != expected
            self.assertEqual(value, True)
        # test different type
        self.assertRaises(TypeError, vuln.__ne__, 5)

    def test_iscomparable(self):
        '''
        test_reportitem: test to throw TypeError in case of uncompatible obj
        '''
        dictvuln = {
            'port': "23456",
            'svc_name': "general",
            'protocol': "tcp",
            'severity': '3',
            'pluginID': '999999',
            'plugin_name': 'XXxxxXXXxXXxXxXxxX',
            }
        expected = NessusReportItem(dictvuln)
        for vuln in self.VulnList:
            value = vuln
            self.assertRaises(TypeError, value.iscomparable, expected)
        # test different type
        self.assertRaises(TypeError, value.iscomparable, 5)

    def test_init(self):
        """test contructor exception when not all param are present"""
        dictvuln = {
            'port': "23456",
            'svc_name': "general",
            'protocol': "tcp",
            'severity': '3',
            }
        self.assertRaises(Exception, NessusReportItem, dictvuln)

    def test_diff(self):
        '''
         test the diff (should return dict of 4 keys)
        '''
        for vuln in self.VulnList:
            value = vuln
            self.assertRaises(TypeError, value.diff, 5)
            value = isinstance(vuln.diff(vuln), dict)
            expected = True
            self.assertEqual(value, expected)
            value = len(vuln.diff(vuln).keys())
            expected = 4
            self.assertEqual(value, expected)

    def test_hash(self):
        expected = 1
        for vuln in self.VulnList:
            object = NessusReportItem(vuln.get_vuln_info.copy())
            a = set()
            a.add(object)
            a.add(object)
            self.assertEqual(len(a), expected)
