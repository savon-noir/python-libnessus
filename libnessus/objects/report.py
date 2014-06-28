#!/usr/bin/env python

from datetime import datetime

from libnessus.objects.dictdiffer import DictDiffer


class NessusReport(object):
    """
        This class represent a Nessus repport, it aims to manipulate
        in a easy way the content, and present some metadata
    """
    def __init__(self, name, hosts):
        '''
        Description: Constructor of NessusReport
        :param name: name of the report
        :type name: str
        :param hosts: list of NessusReportHost
        :type hosts: list
        :return: NessusReport
        :rtype: NessusReport
        '''
        self.name = name
        self.__hosts = hosts
        self.__start = self.__compute_started(self.__hosts)
        self.__end = self.__compute_ended(self.__hosts)

    def __repr__(self):
        '''
        Description: compute a string of the obj
        :return: description de la valeur de retour
        :rtype: str
        '''
        return "{name} {total} {elapsed}".format(name=self.name,
                                                 total=self.hosts_total,
                                                 elapsed=self.elapsed)

    @property
    def hosts(self):
        """Return the list of hosts of the scan
           :return: list
        """
        return self.__hosts

    def save(self, backend):
        '''
        Description: allow to persist to a backend
        :param backend: libnessus.plugins.PluginBackend object.
        :type arg1: PluginBackend
        :return: The primary key of the stored object is returned.
        :rtype: str
        '''
        if backend is not None:
            _id = backend.insert(self)
        else:
            raise RuntimeError
        return _id

    def iscomparable(self, other):
        '''
        description: check if two obj are comparable
        by checking the class name
        :param other: nessusreport
        :type other: nessusreport
        :raises: typeerror if not comparable
        '''
        if not isinstance(other, self.__class__):
            raise TypeError(("non sense incompatibe object : ", self, other))

    def __eq__(self, other):
        '''
        Description: compare obj as equal
        :param other: another report
        :type other: NessusReport
        :return: boolean
        :rtype: boolean
        '''
        try:
            self.iscomparable(other)
            rdict = self.diff(other)
            res_pro = (
                len(rdict["added"]) == 0
                and len(rdict["removed"]) == 0
                and len(rdict["changed"]) == 0
                )
            return res_pro
        except TypeError as etyperr:
            raise etyperr

    def __ne__(self, other):
        '''
        Description: compare obj as !=
        :param other: another report
        :type other: NessusReport
        :return: boolean
        :rtype: boolean
        '''
        try:
            self.iscomparable(other)
            rdict = self.diff(other)
            res_pro = (len(rdict['unchanged']) != len(self.__get_dict()))
            return res_pro
        except TypeError as etyperr:
            raise etyperr

    def __get_dict(self):
        '''
        Description: get a dict representation of the object
        Needed to transform the obj in a dict representation to use dictdiffer
        :return: dict representation of the object
        :rtype: dict
        '''
        rdict = {}
        rdict['name'] = self.name
        hostitem = dict(
            [("%s::%s" % (s.__class__.__name__, s.name), hash(s))
                for s in self.hosts]
            )
        rdict.update(hostitem)
        return rdict

    def diff(self, other):
        '''
        Description: diff object and provide the differences
        :param other: obj to compare to
        :type other: NessusReport
        :return: a dict of all the differences
        :rtype: dict
        '''
        diff = DictDiffer(self.__get_dict(), other.__get_dict())
        rdict = {}
        rdict["removed"] = diff.removed()
        rdict["changed"] = diff.changed()
        rdict["added"] = diff.added()
        rdict["unchanged"] = diff.unchanged()
        return rdict

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
        raise NotImplementedError

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
