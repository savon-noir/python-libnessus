#!/usr/bin/env python
"""
   this code will parse some nessus report, and push them in ElsaticSearch
   This will give the ability to use kibana for analytics
   You need an ES instance running on localhost:9200
   then run this python script from the example dir

"""
from libnessus.parser import NessusParser
from libnessus.plugins.backendpluginFactory import BackendPluginFactory


import glob
from datetime import datetime

url = {'plugin_name': "es"}
backend = BackendPluginFactory.create(**url)
listfiles = "../libnessus/test/files/nessus*"
files = glob.glob(listfiles)

idate = datetime.now().strftime('%Y.%m.%d')
iindex = "nessus-{date}".format(date=idate)
print iindex

for file in files:
    try:
        nessus_obj_list = NessusParser.parse_fromfile(file)
    except:
        continue
    for i in nessus_obj_list.hosts:
        docu = {}
        docu['scantime'] = nessus_obj_list.endtime
        docu['host_ip'] = i.ip
        docu['host_name'] = i.name
        docu['host-fqdn'] = i.get_host_property('host-fqdn')
        docu['operating-system'] = i.get_host_property('operating-system')
        docu['system-type'] = i.get_host_property('system-type')
        for v in i.get_report_items:
            docu['vulninfo'] = v.get_vuln_info
            backend.es.index(index=iindex, doc_type="vulnerability", body=docu)
