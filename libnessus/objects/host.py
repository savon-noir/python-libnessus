#!/usr/bin/env python


class NessusHost(object):
    def __init__(self, host_properties={}, report_items=[]):
        _minimal_attr = set([ 'HOST_START', 'HOST_END', 'host-ip', 'name' ])
        _hostprop_attr = set(host_properties.keys())
        _missing_attr = _minimal_attr.difference(_hostprop_attr)

        if len(_missing_attr) == 0:
            self.__host_properties = host_properties
        else:
            raise Exception("Not all the attributes to create a decent "
                            "NessusHost are available. "
                            "Missing: ".format(" ".join(_missing_attr)))

        self.report_items = report_items

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
        return self.__host_properties

    def get_host_property(self, property_name):
        return self.__host_properties.get(property_name)
