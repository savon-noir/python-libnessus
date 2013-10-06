#!/usr/bin/env python
import xml.etree.ElementTree as ET
from libnessus.objects import NessusHost, NessusReport

class NessusParser(object):
    @classmethod
    def parse(cls, nessus_data, data_type='XML'):
        nessusobj = None

        if not isinstance(nessus_data, str):
            raise Exception("Wrong nessus_data type given as argument: "
                            "Nessus data should be provided as strings")

        if nessus_data and data_type == "XML":
            nessusobj = cls._parse_xml(nessus_data)
        else:
            raise Exception("No or unknown data type provided. Please check "
                            "documentation for supported data types.")
        return nessusobj

    @classmethod
    def _parse_xml(cls, nessus_data=None):
        try:
            root = ET.fromstring(nessus_data)
        except:
            raise Exception("Wrong XML structure: cannot parse data")

        nessusobj = None
        if root.tag == 'NessusClientData':
            nessusobj = cls._parse_xmlv1(root)
        elif root.tag == 'NessusClientData_v2':
            nessusobj = cls._parse_xmlv2(root)
        else:
            raise Exception("Unpexpected data structure for XML root node")
        return nessusobj

    @classmethod
    def _parse_xmlv1(cls, root=None):
        raise Exception("Nessus XML v1 parsing is not supported yet.")

    @classmethod
    def _parse_xmlv2(cls, root=None):
        nessus_reports = []

        for nessus_report in root.findall("Report"):
            nessus_hosts = []
            for nessus_host in nessus_report.findall("ReportHost"):
                _nhost = cls.parse_host(nessus_host)
                nessus_hosts.append(_nhost)

            if 'name' in nessus_report.attrib:
                report_name = nessus_report.attrib['name']
            else:
                report_name = 'unknown'
                sys.stderr.write("warning: Failed to get report name from report")
            nrep = NessusReport(name=report_name, hosts=nessus_hosts)
            nessus_reports.append(nrep)
       
        return nessus_reports

    @classmethod
    def parse_host(cls, root=None):
        _host_name = root.attrib['name'] if 'name' in root.attrib else 'unknown'
    
        _host_prop_elt = root.find("HostProperties")
        _dhp = dict([ (e.attrib['name'], e.text) for e in list(_host_prop_elt) ])
        _dhp.update({'name': _host_name})

        _vuln_list = []
        for report_item in root.findall("ReportItem"):
            _new_item = cls.parse_vulnerability(report_item)
            _vuln_list.append(_new_item)

        return NessusHost(_dhp, _vuln_list)

    @classmethod
    def parse_vulnerability(cls, root=None):
        return root

    @classmethod
    def parse_fromstring(cls, nessus_data, data_type="XML"):
        if not isinstance(nessus_data, str):
            raise Exception("bad argument type for parse_fromstring(): should be a string")
        return cls.parse(nessus_data, data_type)

    @classmethod
    def parse_fromfile(cls, nessus_report_path, data_type="XML"):
        try:
            with open(nessus_report_path, 'r') as fileobj:
                fdata = fileobj.read()
                rval = cls.parse(fdata, data_type)
        except IOError:
            raise
        return rval
