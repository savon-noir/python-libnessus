#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from test_nessus import TestNessus

#from libnessus.parser import NessusParser
from libnessus.plugins.backendplugin import NessusBackendPlugin
from libnessus.plugins.backendpluginFactory import BackendPluginFactory


class TestNessusBackendPlugin(TestNessus):
    """
    This testing class will tests each plugins
    The following test need to be done :
       - test the factory
       - test all the method of the class NessuspBackendPlugin:
          - Verify implmented/notImplemented
          - Verify the behaviour (ie insert must insert)
    To support a new plugin or a new way to instanciate a plugin, add a dict
    with the necessary parameter in the urls table define in setUp
    All testcase must loop thru theses urls to validate a plugins
    """
    def setUp(self):
        TestNessus.setUp(self)
#        fdir = os.path.dirname(os.path.realpath(__file__))
        self.reportList = []
        self.reportList.append(self.forgedreport)

        self.urls = [{'plugin_name': "mongodb"},
                     {'plugin_name': "mongodb", 'dbname': "yoyo", 'store': "patin"},
                     #{'plugin_name':'sql','url':'sqlite://','echo':'debug'},
                     {'plugin_name': 'es',},
                  ]

    def test_backend_factory(self):
        """ test_factory BackendPluginFactory.create(**url)
            Invoke factory and test that the object is of the right classes
        """
        for url in self.urls:
            backend = BackendPluginFactory.create(**url)
            self.assertEqual(isinstance(backend, NessusBackendPlugin), True)
            className = "Nessus%sPlugin" % url['plugin_name'].title()
            print "DEBUUUUUUUUG",className, backend.__class__.__name__
            self.assertEqual(backend.__class__.__name__, className, True)

    def test_backend_factory_Exception(self):
        """ Invoke the factory with dummy value and test the Exception
        """
        self.assertRaises(ImportError, BackendPluginFactory.create, plugin_name="dummy")
        url = {'plugin_name': 'dummy'}
        self.assertRaises(ImportError, BackendPluginFactory.create, **url)
        url = {'plugin_name': 'es', 'host': '192.168.10.10', 'timeout': 2.0}
        self.assertRaises(Exception, BackendPluginFactory.create, **url)
#        url = {'plugin_name': 'es',}
#        self.assertRaises(Exception, BackendPluginFactory.create, **url)

    def test_backend_insert(self):
        """ test_insert
            best way to insert is to call save() of nmapreport :P
            should add some code to test the output as save will catch exception raise by insert
            I dunno how to do that...
        """
        for nrp in self.reportList:
            for url in self.urls:
                #create the backend factory object
                backend = BackendPluginFactory.create(**url)
                #save the report
                returncode = nrp.save(backend)
                #test return code
                self.assertNotEqual(returncode, None)

    def test_backend_get(self):
        """ test_backend_get
            inset all report and save the returned id in a list
            then get each id and create a new list of report
            compare each report (assume eq)
        """
        id_list = []
        result_list = []
        for url in self.urls:
            backend = BackendPluginFactory.create(**url)
            for nrp in self.reportList:
                id_list.append(nrp.save(backend))
            #ES may have 1 second delay between put&get
            time.sleep(1)
            for rep_id in id_list:
                result_list.append(backend.get(rep_id))
            self.assertEqual(len(result_list), len(self.reportList))
            self.assertEqual((result_list), (self.reportList))
            id_list = []
            result_list = []

    def test_backend_getall(self):
        """test_backend_getall
           silly test to be review
        """
        id_list = []
        result_list = []
        for url in self.urls:
            backend = BackendPluginFactory.create(**url)
            for nrp in self.reportList:
                id_list.append(nrp.save(backend))
            #ES may have 1 second delay between put&get
            time.sleep(1)
            result_list = backend.getall()
            print (len(result_list))
            print len(self.reportList)
            self.assertTrue((len(result_list) > 0 ))
            id_list = []
            result_list = []

    def test_backend_delete(self):
        """ test_backend_delete
            inset all report and save the returned id in a list
            for each id remove the item and test if not present
        """
        id_list = []
        result_list = []
        for url in self.urls:
            backend = BackendPluginFactory.create(**url)
            for nrp in self.reportList:
                id_list.append(nrp.save(backend))
            for rep_id in id_list:
                result_list.append(backend.delete(rep_id))
                self.assertEqual(backend.get(rep_id), None)
            id_list = []
            result_list = []


if __name__ == '__main__':
    test_suite = ['test_backend_factory',
                  'test_backend_insert',
                  'test_backend_get',
                  'test_backend_getall',
                  'test_backend_delete'
                  ]
    suite = unittest.TestSuite(map(TestNessusBackendPlugin, test_suite))
    test_result = unittest.TextTestRunner(verbosity=5).run(suite)
