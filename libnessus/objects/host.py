#!/usr/bin/env python


class NessusHost(object):
    def __init__(self, host_properties={}, report_items=[]):
        self._minimal_attr = set(['HOST_START', 'HOST_END', 'host-ip', 'name'])
        self._hostprop_attr = set(host_properties.keys())
        self._missing_attr = self._minimal_attr.difference(self._hostprop_attr)

        if len(self._missing_attr) == 0:
            self.__host_properties = host_properties
        else:
            raise Exception("Not all the attributes to create a decent "
                            "NessusHost are available. "
                            "Missing: ".format(" ".join(self._missing_attr)))

        self.__report_items = report_items

    def __repr__(self):
        """return a string representation of the obj nessusHost"""
        retstr = "{0} {1} {2} {3}".format(self.name,
                                          self.address,
                                          self.get_host_properties(),
                                          self.get_total_vuln())
        return retstr

    @property
    def name(self):
        return self.__host_properties.get('name')

    @property
    def ip(self):
        return self.__host_properties.get('host-ip')

    @property
    def address(self):
        return self.__host_properties.get('host-ip')

    @property
    def started(self):
        return self.__host_properties.get('HOST_START')

    @property
    def ended(self):
        return self.__host_properties.get('HOST_END')

    def get_host_properties(self):
        """Return an dict of properties
           :return: dict
        """
        return self.__host_properties

    def get_hostprop_attr(self):
        """Return a set of keys reprsenting all properties' key
           :return: set
        """
        return self._hostprop_attr

    def get_host_property(self, property_name):
        """return the value of a property
           :param property_name: The name of the property
           :return: str or None
        """
        if property_name in self._hostprop_attr:
            return self.__host_properties.get(property_name)
        else:
            return None

    def get_summary_total_cves(self):
        """Return the number of cve that apply to this host
           :return: int
        """
        return self.get_host_property("patch-summary-total-cves")

    def get_report_items(self):
        """Return an array of vuln"""
        return self.__report_items

    def get_total_vuln(self):
        """Return the number of vulnerability (reportitem)"""
        return len(self.__report_items)
