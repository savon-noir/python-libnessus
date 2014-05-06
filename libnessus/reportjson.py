#!/usr/bin/env python
import json
from libnessus.objects import NessusHost, NessusReportItem, NessusReport
from libnessus.parser import NessusParser


class ReportEncoder(json.JSONEncoder):
    def default(self, obj):
        otype = {'NessusHost': NessusHost,
                 'NessusReportItem': NessusReportItem,
                 'NessusReport': NessusReport}
        if isinstance(obj, tuple(otype.values())):
            key = "__{0}__".format(obj.__class__.__name__)
            return {key: obj.__dict__}
        return json.JSONEncoder.default(self, obj)


class ReportDecoder(json.JSONDecoder):
    def decode(self, json_str):
        r = NessusParser.parse_fromdict(json.loads(json_str))
        return r
