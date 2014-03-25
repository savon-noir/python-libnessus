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
        self.__start = self.__compute_started(self.__hosts)
        self.__end = self.__compute_ended(self.__hosts)

    @property
    def hosts(self):
        """Return the list of hosts of the scan
           :return: list
        """
        return self.__hosts

    def save(self, backend):
        pass

    def diff(self, other):
        pass

    @property
    def started(self):
        """Return started property
           :return: datetime
        """
        return self.__start

    @staticmethod
    def __compute_started(hosts):
        """Find the start of the scan by checking all host HOST_START"""
        list_date = []
        for host in hosts:
            date_object = datetime.strptime(
                host.started, '%a %b %d %H:%M:%S %Y')
            list_date.append(date_object)
        list_date.sort()
        return list_date[0]

    @property
    def endtime(self):
        """Return ended property
           :return: datetime
        """
        return self.__end

    @staticmethod
    def __compute_ended(hosts):
        """Find the end of the scan by checking all host HOST_END"""
        list_date = []
        for host in hosts:
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
        return self.__end - self.__start

    @property
    def hosts_total(self):
        """Get the total number of hosts
           :return: int
        """
        return len(self.__hosts)
