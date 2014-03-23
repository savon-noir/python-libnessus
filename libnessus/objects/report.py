#!/usr/bin/env python

from datetime import datetime


class NessusReport(object):
    """
        This class represent a Nessus repport, it aims to manipulate
        in a easy way the content, and present some metadata
    """
    def __init__(self, name, hosts):
        """Constructor get a name and an array of hosts"""
        self.name = name
        self.__hosts = hosts

    @property
    def hosts(self):
        return self.__hosts

    def save(self, backend):
        pass

    def diff(self, other):
        pass

    @property
    def started(self):
        """Find the start of the scan by checking all host HOST_START"""
        list_date = []
        for host in self.__hosts:
            date_object = datetime.strptime(
                host.started, '%a %b %d %H:%M:%S %Y')
            list_date.append(date_object)
        list_date.sort()
        return list_date[0]

#    @property
#    def commandline(self):
#        pass
#
#    @property
#    def version(self):
#        pass
#
#    @property
#    def scan_type(self):
#        pass
#
#    def get_host_byid(self, host_id):
#        pass

    @property
    def endtime(self):
        """Find the end of the scan by checking all host HOST_START"""
        list_date = []
        for host in self.__hosts:
            date_object = datetime.strptime(
                host.ended, '%a %b %d %H:%M:%S %Y')
            list_date.append(date_object)
        list_date.sort()
        return list_date[len(list_date)-1]

    @property
    def summary(self):
        pass

    @property
    def elapsed(self):
        """Return the amount of time of the test
           :return: datetime
        """
        return self.endtime - self.started

#    @property
#    def hosts_up(self):
#        pass
#
#    @property
#    def hosts_down(self):
#        pass

    @property
    def hosts_total(self):
        """Get the total number of hosts
           :return: int
        """
        return len(self.__hosts)

#    def get_raw_data(self):
#        pass
