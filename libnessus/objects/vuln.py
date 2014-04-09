#!/usr/bin/env python


class NessusVuln(object):
    """This class represent a ReportItem in the nessus xml"""
    def __init__(self, vuln_info={}):
        """Constructor of Vulnerability
           :param vuln_info: dict of vulnerabities
        """
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
        """
        Get the port where the vuln is detected, 0 if not network detected
        :return str
        """
        return self.__vuln_info['port']

    @property
    def service(self):
        """
        Get the service name if known
        :return str
        """
        return self.__vuln_info['svc_name']

    @property
    def protocol(self):
        """
        Get the protocol
        :return str
        """
        return self.__vuln_info['protocol']

    @property
    def severity(self):
        """
        Get Severity level, It corresponds with a
        "0" as an open port,
        "1" as a low or informational
        "2" as a medium or warning and
        "3" as a high or hole
        return str
        """
        return self.__vuln_info['severity']

    @property
    def plugin_id(self):
        """
        Get the plugin id
        :return str
        """
        return self.__vuln_info['plugin']['plugin_id']

    @property
    def plugin_name(self):
        """
        Get the plugin Name
        :return str
        """
        return self.__vuln_info['plugin']['plugin_name']

    @property
    def plugin_family(self):
        """
        Get the test Family
        :return str
        """
        return self.__vuln_info['plugin']['plugin_family']

    @property
    def get_vuln_info(self):
        """
        Get a dict of the whole vulnerability
        :return dict
        """
        return self.__vuln_info

    @property
    def get_vuln_risk(self):
        """
        Get a dict of the risk
        :return dict
        """
        return self.__vuln_info['risk_score']

    @property
    def get_vuln_plugin(self):
        """
        Get a dict of plugin
        :return dict
        """
        return self.__vuln_info['plugin']

    @property
    def get_vuln_xref(self):
        """
        Get a dict of xref
        :return dict
        """
        return self.__vuln_info['vuln_ref']

    @property
    def synopsis(self):
        """
        Get the sypnosis of the vuln
        :return str
        """
        return self.__vuln_info['synopsis']

    @property
    def description(self):
        """
        Get description
        :return str
        """
        return self.__vuln_info['description']

    @property
    def solution(self):
        """
        Get the sulution provide by nessus
        :return str
        """
        return self.__vuln_info['solution']
