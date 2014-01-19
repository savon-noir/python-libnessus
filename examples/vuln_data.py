#!/usr/bin/env python

from libnessus.parser import NessusParser

nessus_obj_list = NessusParser.parse_fromfile('/vagrant/nessus.xml')

vuln_data = {'Info': 0, 'Low': 0, 'Medium': 0, 'High': 0, 'Critical': 0}
risk_labels = ['Info', 'Low', 'Medium', 'High', 'Critical']

for nessuso in nessus_obj_list:
    for _host in nessuso.hosts:
        for _vuln in _host.report_items:
            try:
                vuln_data[risk_labels[int(_vuln.severity)]] += 1
            except ValueError:
                print "Failed to convert severity id to integer: report corrupted."
print vuln_data
