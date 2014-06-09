import requests
import json
from random import randint


class NessusAPI(object):
    """
        NessusAPI is the class providing the methods for the nessus API.
        It is responsible for managing scans, scan policies and users.
    """
    def __init__(self, host="127.0.0.1", port=8834):
        """
            Constructor of NmapAPI class.

            :param host: IP/hostname of the API host
            :type host: string

            :param port: port of the API on host
            :type port: int

            :return: NmapAPI object
        """
        self.host = host
        self.port = port

    def api_url(self, service=''):
        return "https://{0}:{1}/{2}".format(self.host, self.port, service)

    def authenticate(self, login='', password=''):
        """
            Method to authenticate to the remote API host.
        """
        headers = {'content-type': 'application/json'}
        payload = {'login': login, 'password': password, 'seq': self.get_seq()}
        req = requests.post(self.api_url,
                            data=json.dumps(payload),
                            headers=headers)
        return req

    def get_seq(self):
        return randint(1024, 65535)
