from elasticsearch import Elasticsearch
import jsonpickle
import datetime
import base64

from libnessus.plugins.backendplugin import NessusBackendPlugin


class NessusEsPlugin(NessusBackendPlugin):
    """
      This class handle the persistence of NessusReport object in ElasticSearc
      Implementation is made using ElasticSearch python module
      Object of this class must be create via the
      BackendPluginFactory.create(**url) where url is a named dict like
      {'plugin_name': "es"} this dict may receive all the param
      Elasticsearch() support
    """
    def __init__(self, dbname=None, store=None, **kwargs):
        NessusBackendPlugin.__init__(self)
        try:
            self.dbname = 'nessus'
            self.store = 'reports'
            self.index = "{db}_{store}".format(
                db=self.dbname,
                store=self.store)
            self.es = Elasticsearch(**kwargs)
            self.es.indices.create(index=self.index, ignore=400)
        except:
            raise

    def insert(self, report):
        """
            insert NessusReport in the backend
            :param NessusReport:
            :return: str the ident of the object in the backend for
            future usage
            or None
        """
        j = jsonpickle.encode(report, unpicklable=False)
        j2 = jsonpickle.encode(report).encode('utf-8')
        b64 = base64.b64encode(j2).decode(encoding='UTF-8')
        docid = hash(report.name)
        docu = {"hash": docid,
                "json": j,
                "json_base64": b64,
                "date": datetime.datetime.utcnow(),
                "name": report.name,
                "endtime": report.endtime,
                "ipaddress": [host.address for host in report.hosts]}
        try:
            self.es.index(
                index=self.index,
                doc_type=self.store,
                body=docu,
                id=docid
                )
            return docid
        except:
            raise

    def delete(self, myid):
        """
            delete NessusReport if the backend
            :param id: str
            :return: bool
        """
        rc = self.es.delete(
            index=self.index,
            doc_type=self.store,
            id=myid)
        return rc['found']

    def get(self, id):
        """
            retreive a NessusReport from the backend
            :param id: str
            :return: NessusReport or None
        """
        report = None
        filter = {"match": {"_id": id}}
        ret = self.getall(filter=filter)
        if len(ret) == 1:
            id, report = ret[0]
        return report

    def getall(self, filter={"match_all": {}}, limit=30, qfrom=0):
        """
            :return: collection of tuple (id,NessusReport)
            :param filter: a dict that will be added to match_all
            ie : {"match": {"_id": id}}
            :type dict_filter: dict
            :param limit: max number of result allowed
            :type limit: int
            :param qfrom: offset into results
            :type qfrom: int
        """
        nessusreportlist = []
        rsearch = self.es.search(
            index=self.index,
            body={
                "from": qfrom,
                "size": limit,
                "query": filter,
                "_source": ["json_base64"]})
        if rsearch['hits']['total'] > 0:
            for hit in rsearch['hits']['hits']:
                srcdict = hit['_source']
                b64 = srcdict['json_base64']
                b64 = b64.encode('utf-8')
                pickle = base64.b64decode(b64).decode('utf-8')
                id = hit['_id']
                nessusreport = jsonpickle.decode(pickle)
                nessusreportlist.append((id, nessusreport))
        return nessusreportlist
