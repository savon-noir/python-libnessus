#!/usr/bin/env python
import xml.etree.ElementTree as ET
from libnessus.objects import NessusHost, NessusVuln, NessusReport


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
        """
            This private method will return 0 or one report
            (as describe in nessus's doc)
            :param root: a string representing a part or a complete nessus scan
            :return: NessusReport or None
        """
        nrp = None

        for nessus_report in root.findall("Report"):
            nessus_hosts = []
            for nessus_host in nessus_report.findall("ReportHost"):
                _nhost = cls.parse_host(nessus_host)
                nessus_hosts.append(_nhost)

            if 'name' in nessus_report.attrib:
                report_name = nessus_report.attrib['name']
            else:
                report_name = 'none'
                print("warning: Failed to get report name from report")
            nrp = NessusReport(name=report_name, hosts=nessus_hosts)

        return nrp

    @classmethod
    def parse_host(cls, root=None):
        _host_name = root.attrib['name'] if 'name' in root.attrib else 'none'
        #print _host_name
        #print root.attrib

        _host_prop_elt = root.find("HostProperties")
        _dhp = dict([(e.attrib['name'], e.text) for e in list(_host_prop_elt)])
        _dhp.update({'name': _host_name})

        _vuln_list = []
        for report_item in root.findall("ReportItem"):
            _new_item = cls.parse_vulnerability(report_item)
            _vuln_list.append(_new_item)

        return NessusHost(_dhp, _vuln_list)

    @classmethod
    def parse_vulnerability(cls, root=None):
        _vuln_data = {
            'port': root.attrib.get('port'),
            'svc_name': root.attrib.get('svc_name'),
            'protocol': root.attrib.get('protocol'),
            'severity': root.attrib.get('severity'),
            'plugin': {
                'plugin_id': root.attrib.get('pluginId'),
                'plugin_name': root.attrib.get('pluginName'),
                'plugin_family': root.attrib.get('pluginFamily'),
            },
            'risk_score': {},
            'vuln_ref': {'cve': [], 'cwe': [], 'bid': [], 'osvdb': [],
                         'iava': [], 'iavb': [], 'cert': [], 'xref': []
                         }
        }

        for elt in root:
            if 'plugin_' in elt.tag or 'script_version' in elt.tag:
                _vuln_data['plugin'].update({elt.tag: elt.text})
            elif elt.tag == 'risk_factor' or 'cvss_' in elt.tag:
                _vuln_data['risk_score'].update({elt.tag: elt.text})
            elif elt.tag in ['cve', 'bid', 'osvdb', 'iava', 'iavb', 'xref']:
                _vuln_data['vuln_ref'][elt.tag].append(elt.text)
            else:
                _vuln_data.update({elt.tag: elt.text})

        return NessusVuln(_vuln_data)

    @classmethod
    def parse_fromstring(cls, nessus_data, data_type="XML"):
        if not isinstance(nessus_data, str):
            raise Exception("bad argument type : should be a string")
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

    @classmethod
    def parse_fromdict(cls, rdict):
        nreport = {}

        rdict = rdict.pop()
        try:
            if rdict.keys()[0] == '__NessusReport__':
                r = rdict['__NessusReport__']
                rname = r['name']

                hlist = []
                for _host in r['_NessusReport__hosts']:
                    _vlist = []
                    for _vulns in _host['__NessusHost__']['report_items']:
                        _vdictdata =\
                            _vulns['__NessusVuln__']['_NessusVuln__vuln_info']
                        _vlist.append(NessusVuln(_vdictdata))

                    _dhp =\
                        _host['__NessusHost__']['_NessusHost__host_properties']
                    nh = NessusHost(_dhp, _vlist)
                    hlist.append(nh)
                nreport = NessusReport(name=rname, hosts=hlist)
        except KeyError:
            raise
        return nreport
