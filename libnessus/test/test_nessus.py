#!/usr/bin/env python

import unittest
import os
from libnessus.parser import NessusParser


class TestNessus(unittest.TestCase):
    '''TestNEssus class only contains the setUp functions all test class will
       inherit from this one'''
    def setUp(self):
        '''setup a table of report based on the files in flist '''
        self.fdir = os.path.dirname(os.path.realpath(__file__))
        self.flist = [
            {'file': "%s/%s" % (self.fdir, 'files/nessus_report_local2.nessus'),
             'hosts': 1,
             'rep_start': "Fri Oct  4 15:06:24 2013",
             'rep_end': "Fri Oct  4 15:07:30 2013",
             'hosts_ip': ["127.0.0.1", ],
             'hosts_start': ["Fri Oct  4 15:06:24 2013", ],
             'hosts_end': ["Fri Oct  4 15:07:30 2013", ],
             'patch-summary-total-cves': ["0"],
             'totalVulnPerHost': [62],
             'hosts_names': ["localhost", ]},
            {'file': "%s/%s" % (self.fdir, 'files/nessus_report_localpci.nessus'),
             'hosts': 1,
             'rep_start': "Tue Jan  7 08:19:20 2014",
             'rep_end': "Tue Jan  7 08:19:25 2014",
             'hosts_ip': ["127.0.0.1", ],
             'hosts_start': ["Tue Jan  7 08:19:20 2014", ],
             'hosts_end': ["Tue Jan  7 08:19:25 2014", ],
             'patch-summary-total-cves': ["156"],
             'totalVulnPerHost': [167],
             'hosts_names': ["127.0.0.1", ]},
            {'file': "%s/%s" % (self.fdir, 'files/nessus_report_test_local.nessus'),
             'hosts': 2,
             'rep_start': "Tue Oct  1 18:19:31 2013",
             'rep_end': "Wed Oct  2 09:03:58 2013",
             'hosts_ip': ["192.168.1.3", "192.168.1.1"],
             'hosts_start': ["Tue Oct  1 18:19:31 2013",
                             "Tue Oct  1 18:19:31 2013"],
             'hosts_end': ["Tue Oct  1 18:20:43 2013",
                           "Wed Oct  2 09:03:58 2013"],
             'patch-summary-total-cves': ["31","14"],
             'totalVulnPerHost': [74, 73],
             'hosts_names': ["192.168.1.3", "192.168.1.1"]},
            {'file': "%s/%s" % (self.fdir, 'files/nessus_report_local_3.nessus'),
             'hosts': 3,
             'rep_start': "Thu Mar 20 00:30:57 2014",
             'rep_end': "Thu Mar 20 01:22:17 2014",
             'hosts_start': ["Thu Mar 20 00:30:57 2014",
                             "Thu Mar 20 00:30:57 2014",
                             "Thu Mar 20 00:30:57 2014"],
             'hosts_end': ["Thu Mar 20 01:07:03 2014",
                           "Thu Mar 20 00:57:04 2014",
                           "Thu Mar 20 01:22:17 2014"],
             'patch-summary-total-cves': ["0","9","43"],
             'totalVulnPerHost': [2,31,73],
             'hosts_ip': ["192.168.2.104", "192.168.2.101", "192.168.2.100"],
             'hosts_names': ["192.168.2.104", "192.168.2.101", "192.168.2.100"]},
        ]
        #parse them once and for all
        for testfile in self.flist:
            fd = open(testfile['file'], 'r')
            s = fd.read()
            fd.close()
            nrp = NessusParser.parse(s)
            testfile['report'] = nrp
        #cannot parse these file as it will provoque an excepetion
        self.badlist = [
            {'file': "%s/%s" % (self.fdir, 'files/xxxxxxxx.nessus'),
             'hosts': 0},
            ]
        #special report for Vuln Testing one host many vuln
        self.expected_vuln = [
            {
                'port': "0",
                'svc_name': "general",
                'protocol': "tcp",
                'severity': "0",
                'plugin_id': "19506",
                'plugin_name': "Nessus Scan Information",
                'plugin_family': "Settings",
                'plugin_modification_date': "2013/11/21",
                'plugin_publication_date': '2005/08/26',
                'risk_factor': "None",
                'solution': 'n/a',
                'synopsis': 'Information about the Nessus scan.',
            },
            {
                'port': '0',
                'protocol': 'tcp',
                'severity': '0',
                'solution': 'Install the patches listed below',
                'svc_name': 'general',
                'synopsis': 'The remote host is missing several patches',
                'risk_factor': 'None',
                'plugin_family': 'General',
                'plugin_id': '66334',
                'plugin_modification_date': '2013/12/18',
                'plugin_name': 'Patch Report',
                'plugin_publication_date': '2013/05/07',
                'plugin_type': 'local',
            },
            {
                'port': '0',
                'protocol': 'tcp',
                'risk_factor': 'None',
                'severity': '0',
                'solution': 'n/a',
                'svc_name': 'general',
                'synopsis': 'Notes the proper handling of false positives in PCI DSS scans.',
                'plugin_family': 'Policy Compliance',
                'plugin_id': '60020',
                'plugin_modification_date': '2012/07/05',
                'plugin_name': 'PCI DSS Compliance : Handling False Positives',
                'plugin_publication_date': '2012/07/18',
                'plugin_type': 'summary',
            },
            {
                'severity': '4',
                'solution': 'Upgrade to the latest version of rpc.statd.',
                'svc_name': 'rpc-status',
                'synopsis': 'The remote service is vulnerable to a buffer overflow.',
                'port': '33489',
                'protocol': 'udp',
                'risk_factor': 'Critical',
                'plugin_id': '10544',
                'plugin_modification_date': '2012/06/22',
                'plugin_name': 'Linux Multiple statd Packages Remote Format String',
                'plugin_family': 'RPC',
                'plugin_publication_date': '2000/11/10',
                'plugin_type': 'remote',
            },
            {
                'severity': '3',
                'solution': 'Update the affected nspr packages.',
                'svc_name': 'general',
                'synopsis': 'The remote CentOS host is missing one or more security updates.',
                'port': '0',
                'protocol': 'tcp',
                'risk_factor': 'High',
                'plugin_family': 'CentOS Local Security Checks',
                'plugin_id': '64381',
                'plugin_modification_date': '2013/06/29',
                'plugin_name': 'CentOS 6 : nspr (CESA-2013:0213)',
                'plugin_publication_date': '2013/02/01',
                'plugin_type': 'local',
            }
            ]

        fd = open("%s/%s" % (self.fdir, 'files/nessus_forgedReport_ReportItem.nessus'))
        s = fd.read()
        fd.close()
        nrp = NessusParser.parse(s)
        self.VulnList = nrp.hosts[0].get_report_items
