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
import logging

from datetime import datetime

# parse args
parser = argparse.ArgumentParser(
    description='This script will load nessusV2 report in an ES datastore')
parser.add_argument('--filename',
                    default="../libnessus/test/files/nessus*",
                    help="path or pattern to a nessusV2 xml")
parser.add_argument('--es_trace',
                    default="/dev/null",
                    help="elasticsearch tracefile location")
args = parser.parse_args()

url = {'plugin_name': "es"}
backend = BackendPluginFactory.create(**url)
index_settings = {u'mappings': {u'vulnerability': {u'properties': {u'host-fqdn': {u'type': u'string'},
    u'host_ip': {u'type': 'ip'},
    u'host_name': {u'type': u'string'},
    u'operating-system': {u'type': u'string'},
    u'scantime': {u'format': u'dateOptionalTime', u'type': u'date'},
    u'system-type': {u'type': u'string'},
    u'vulninfo': {u'properties': {u'apple-sa': {u'type': u'string'},
      u'bid': {u'type': u'string'},
      u'canvas_package': {u'type': u'string'},
      u'cert': {u'type': u'string'},
      u'cpe': {u'type': u'string'},
      u'cve': {u'type': u'string'},
      u'cvss_base_score': {u'type': u'float'},
      u'cvss_temporal_score': {u'type': u'string'},
      u'cvss_temporal_vector': {u'type': u'string'},
      u'cvss_vector': {u'type': u'string'},
      u'cwe': {u'type': u'string'},
      u'd2_elliot_name': {u'type': u'string'},
      u'description': {u'type': u'string'},
      u'edb-id': {u'type': u'string'},
      u'exploit_available': {u'type': u'boolean'},
      u'exploit_framework_canvas': {u'type': u'string'},
      u'exploit_framework_core': {u'type': u'string'},
      u'exploit_framework_d2_elliot': {u'type': u'string'},
      u'exploit_framework_metasploit': {u'type': u'string'},
      u'exploitability_ease': {u'type': u'string'},
      u'exploited_by_malware': {u'type': u'string'},
      u'fname': {u'type': u'string'},
      u'iava': {u'type': u'string'},
      u'iavb': {u'type': u'string'},
      u'metasploit_name': {u'type': u'string'},
      u'osvdb': {u'type': u'string'},
      u'owasp': {u'type': u'string'},
      u'patch_publication_date': {u'format': u'yyyy/MM/dd HH:mm:ss||yyyy/MM/dd',
       u'type': u'date'},
      u'pluginFamily': {u'type': u'string'},
      u'pluginID': {u'type': u'string'},
      u'pluginName': {u'type': u'string'},
      u'plugin_modification_date': {u'format': u'yyyy/MM/dd HH:mm:ss||yyyy/MM/dd',
       u'type': u'date'},
      u'plugin_name': {u'type': u'string'},
      u'plugin_output': {u'type': u'string'},
      u'plugin_publication_date': {u'format': u'yyyy/MM/dd HH:mm:ss||yyyy/MM/dd',
       u'type': u'date'},
      u'plugin_type': {u'type': u'string'},
      u'port': {u'type': u'string'},
      u'protocol': {u'type': u'string'},
      u'rhsa': {u'type': u'string'},
      u'risk_factor': {u'type': u'string'},
      u'script_version': {u'type': u'string'},
      u'secunia': {u'type': u'string'},
      u'see_also': {u'type': u'string'},
      u'severity': {u'type': u'integer'},
      u'solution': {u'type': u'string'},
      u'stig_severity': {u'type': u'string'},
      u'svc_name': {u'type': u'string'},
      u'synopsis': {u'type': u'string'},
      u'vuln_publication_date': {u'format': u'yyyy/MM/dd HH:mm:ss||yyyy/MM/dd',
       u'type': u'date'},
      u'xref': {u'type': u'string'}}}}}}} 

# get trace logger and set level
tracer = logging.getLogger('elasticsearch.trace')
tracer.setLevel(logging.ERROR)
tracer.addHandler(logging.FileHandler(args.es_trace))

listfiles = args.filename
print listfiles
files = glob.glob(listfiles)

idate = datetime.now().strftime('%Y.%m.%d')
iindex = "nessus-{date}".format(date=idate)
backend.es.indices.create(index=iindex,
                  body=index_settings,
                  ignore=400
                  )
print iindex

for file in files:
    try:
        nessus_obj_list = NessusParser.parse_fromfile(file)
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
    print "file imported successfully : %s" % file
