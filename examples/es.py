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
import argparse

from datetime import datetime

# parse args
parser = argparse.ArgumentParser(
    description='This script will load nessusV2 report in an ES datastore')
parser.add_argument('--filename',
                    default="../libnessus/test/files/nessus*",
                    help="path or pattern to a nessusV2 xml")
args = parser.parse_args()

url = {'plugin_name': "es"}
backend = BackendPluginFactory.create(**url)

listfiles = args.filename
print listfiles
files = glob.glob(listfiles)

idate = datetime.now().strftime('%Y.%m.%d')
iindex = "nessus-{date}".format(date=idate)
print iindex

for file in files:
    try:
        nessus_obj_list = NessusParser.parse_fromfile(file)
        print "file imported successfully : %s" % file
    except:
        print "file cannot be imported : %s" % file
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
