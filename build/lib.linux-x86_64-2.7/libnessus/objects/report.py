

class NessusReport(object):
    def __init__(self, name, hosts):
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
        pass

    @property
    def commandline(self):
        pass

    @property
    def version(self):
        pass

    @property
    def scan_type(self):
        pass

    def get_host_byid(self, host_id):
        pass

    @property
    def endtime(self):
        pass

    @property
    def summary(self):
        pass

    @property
    def elapsed(self):
        pass

    @property
    def hosts_up(self):
        pass

    @property
    def hosts_down(self):
        pass

    @property
    def hosts_total(self):
        pass

    def get_raw_data(self):
        pass
