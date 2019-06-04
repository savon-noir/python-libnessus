#!/usr/bin/env python
"""
File: reporthost.py
Author: Me
Description:
"""

from libnessus.objects.dictdiffer import DictDiffer
from libnessus.objects import reportlogger
from libnessus import exceptions as NessusExceptions

log = reportlogger.ReportLogger

class NessusReportHost(object):
    """
    Description: Represent an object NessusReportHost in a nessus xml
    """
    def __init__(self, host_properties={}, report_items=[]):
        _minimal_attr = set(['HOST_START', 'HOST_END', 'host-ip', 'name'])
        self._hostprop_attr = set(host_properties.keys())
        _missing_attr = _minimal_attr.difference(self._hostprop_attr)

        if len(_missing_attr) == 0:
            self.__host_properties = host_properties
        else:
            log.debug("Host Missing Attributes: ")
            log.debug(host_properties)
            raise NessusExceptions.MissingAttribute("Not all the attributes to create a decent "
                            "NessusReportHost are available. "
                            "Missing: {}".format(" ".join(_missing_attr)))

        self.__report_items = report_items

    def __repr__(self):
        """return a string representation of the obj nessusHost"""
        return "{0} {1} {2} {3}".format(self.name, self.address, self.get_host_properties, self.get_total_vuln)

    def __hash__(self):
        """:return: hash function to be able to add object to dict/set
           :rtype: hash
        """
        return hash(self.address)

    def iscomparable(self, other):
        """
        Description: check if two obj are comparable
        by checking the class name and adress value are equal
        :param other: NessusReportHost
        :type other: NessusReportHost
        :raises: TypeError if not comparable
        """
        if not isinstance(other, self.__class__):
            raise TypeError(("Non sense incompatibe object : ", self, other))
        if self.address != other.address:
            raise TypeError(("Address need to be == : ", self, other))

    def __eq__(self, other):
        """
        Description: compare all properties and reportitem
        :param other: the object to compare
        :type other: NessusReportHost
        :return: true if equal
        :rtype: boolean
        """
        try:
            self.iscomparable(other)
        except TypeError as etyperr:
            raise etyperr
        rdict = self.diff(other)
        res_pro = (
            len(rdict["added"]) == 0 and
            len(rdict["removed"]) == 0 and
            len(rdict["changed"]) == 0
            )
        return res_pro

    def __ne__(self, other):
        """
        Description:
        :param other: the object to compare
        :type other: NessusReportHost
        :return: true if equal
        :rtype: boolean
        """
        try:
            self.iscomparable(other)
        except TypeError as etyperr:
            raise etyperr
        rdict = self.diff(other)
        res_pro = (len(rdict['unchanged']) != len(self.__get_dict()))
        return res_pro

    def __get_dict(self):
        """
        Description: get a dict representation of the object
        Needed because the object has 2 main component :
        a dict and a table of ReportItem
        :return: dict representation of the object
        :rtype: dict
        """
        rdict = self.get_host_properties.copy()
        # add reportitem in the dict in the form
        # key = {'NessusReportItem::10544': NessusReportItem,}
        reportitem = dict(
            [("%s::%s" % (s.__class__.__name__, str(s.plugin_id)), s)
                for s in self.__report_items]
            )
        rdict.update(reportitem)
        return rdict

    def diff(self, other):
        """
        Description: compute a diff dict obj
        :param other: the object to compare
        :type other: NessusReportHost
        :return:
        :rtype: dict
        """
        diff = DictDiffer(self.__get_dict(), other.__get_dict())
        rdict = {}
        rdict["removed"] = diff.removed()
        rdict["changed"] = diff.changed()
        rdict["added"] = diff.added()
        rdict["unchanged"] = diff.unchanged()
        return rdict

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

    @property
    def get_host_properties(self):
        """Return an dict of properties
           :return: dict
        """
        return self.__host_properties

    @property
    def get_hostprop_attr(self):
        """Return a set of keys representing all properties' key
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

    @property
    def get_summary_total_cves(self):
        """Return the number of cve that apply to this host
           :return: int
        """
        return self.get_host_property("patch-summary-total-cves")

    @property
    def get_report_items(self):
        """Return an array of vuln"""
        return self.__report_items

    @property
    def get_total_vuln(self):
        """Return the number of vulnerability (reportitem)"""
        return len(self.__report_items)
