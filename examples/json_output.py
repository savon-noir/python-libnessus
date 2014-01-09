from libnessus.parser import NessusParser
from pprint import pprint

nessus_obj_list = NessusParser.parse_fromfile('/vagrant/nessus.xml')

vuln_data = {'Info': 0, 'Low': 0, 'Medium': 0, 'High': 0, 'Critical': 0}
risk_labels = ['Info', 'Low', 'Medium', 'High', 'Critical']
owner = 'test0r'

reports = []
for nessuso in nessus_obj_list:
    jnreport = { 'name': '', 'started': '', 'ended': '', 'owner': 'test0r', 'hosts': [] }
    jnreport['name'] = nessuso.name
    jnreport['started'] = nessuso.hosts[0].started
    jnreport['ended'] = nessuso.hosts[len(nessuso.hosts)-1].ended
    for _host in nessuso.hosts:
        jnhost = { 'name': '', 'address': '', 'started': '', 'ended': '', 'vulns': []}
        for _hk in jnhost.keys():
            if _hk != 'vulns':
                jnhost[_hk] = getattr(_host, _hk)
        for _vuln in _host.report_items:
            jnvuln = { 'port': '', 'protocol': '', 'service': '',
                       'severity': '', 'plugin_id': '', 'plugin_name': ''
            }
            for _vk in jnvuln.keys():
                jnvuln[_vk] = getattr(_vuln, _vk)
            jnhost['vulns'].append(jnvuln)
        jnreport['hosts'].append(jnhost)
    reports.append(jnreport)

pprint(reports)
#            except ValueError:
#                print "Failed to convert severity id to integer: report corrupted."
#print vuln_data
