#!/usr/bin/env python


class NessusVuln(object):
    def __init__(self, vuln_info={}):
        _minimal_attr = set(['port', 'svc_name', 'protocol', 'severity'])

        _vuln_info_attr = set(vuln_info.keys())
        _missing_attr = _minimal_attr.difference(_vuln_info_attr)

        if len(_missing_attr) == 0:
            self.__vuln_info = vuln_info
        else:
            raise Exception("Not all the attributes to create a decent "
                            "NessusVuln object are available. "
                            "Missing: ".format(" ".join(_missing_attr)))

    @property
    def port(self):
        return self.__vuln_info['port']

    @property
    def service(self):
        return self.__vuln_info['svc_name']

    @property
    def protocol(self):
        return self.__vuln_info['protocol']

    @property
    def severity(self):
        return self.__vuln_info['severity']

    @property
    def plugin_id(self):
        return self.__vuln_info['plugin']['plugin_id']

    @property
    def plugin_name(self):
        return self.__vuln_info['plugin']['plugin_name']

    @property
    def plugin_family(self):
        return self.__vuln_info['plugin']['plugin_family']

    @property
    def get_vuln_info(self):
        return self.__vuln_info

    @property
    def get_vuln_risk(self):
        return self.__vuln_info['risk_score']

    @property
    def get_vuln_plugin(self):
        return self.__vuln_info['plugin']

    @property
    def get_vuln_xref(self):
        return self.__vuln_info['vuln_ref']

    @property
    def synopsis(self):
        return self.__vuln_info['synopsis']

    @property
    def description(self):
        return self.__vuln_info['description']

    @property
    def solution(self):
        return self.__vuln_info['solution']
