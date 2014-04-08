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
        """"""
    def test_protocol(self):
        """"""
    def test_severity(self):
        """"""
    def test_plugin_id(self):
        """"""
    def test_plugin_name(self):
        """"""
    def test_plugin_family(self):
        """"""
    def test_get_vuln_info(self):
        """"""
    def test_get_vuln_risk(self):
        """"""
    def test_get_vuln_plugin(self):
        """"""
    def test_get_vuln_xref(self):
        """"""
    def test_synopsis(self):
        """"""
    def test_description(self):
        """"""
    def test_solution(self):
        """"""
