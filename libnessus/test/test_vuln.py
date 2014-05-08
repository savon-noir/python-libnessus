#!/usr/bin/env python

from test_nessus import TestNessus


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
            value = vuln
            expected = vuln
            self.assertEqual(value, expected)

