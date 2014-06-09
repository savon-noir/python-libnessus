#!/usr/bin/env python


class NessusBackendPlugin(object):
    """
        Abstract class showing to the minimal implementation for a plugin
        All subclass MUST at least implement the following methods
    """
    def __init__(self):
        self.dbname = 'nessus'
        self.store = 'reports'

    def insert(self, NessusReport):
        """
            insert NessusReport in the backend
            :param NessusReport:
            :return: str the ident of the object in the backend for
            future usage
            or None
        """
        raise NotImplementedError

    def delete(self, id):
        """
            delete NessusReport if the backend
            :param id: str
        """
        raise NotImplementedError

    def get(self, id):
        """
            retreive a NessusReport from the backend
            :param id: str
            :return: NessusReport
        """
        raise NotImplementedError

    def getall(self, filter):
        """
            :return: collection of tuple (id,NessusReport)
            :param filter: Nice to have implement a filter capability
        """
        raise NotImplementedError
