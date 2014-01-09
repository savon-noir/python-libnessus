from libnessus.parser import NessusParser
from libnessus.reportjson import ReportEncoder
import json
from pprint import pprint

nessus_obj_list = NessusParser.parse_fromfile('/vagrant/nessus.xml')
for nessuso in nessus_obj_list:
    pprint(json.dumps(nessuso, cls=ReportEncoder))
