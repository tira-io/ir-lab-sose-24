import importlib
create_qrel_details = importlib.import_module('construct_topics_for_ui').create_qrel_details
import unittest
from approvaltests.approvals import verify
import os

def resource(f):
    return os.path.dirname(os.path.realpath(__file__)) + '/resources/' + f


class TestCreationOfQrelDetails(unittest.TestCase):
    def test_parsing_of_documents_without_runs(self):
        verify(create_qrel_details('vaswani', {})[:1])

    def test_parsing_of_documents_with_two_runs(self):
        verify(create_qrel_details('vaswani', {'a': resource('run-vaswani-dummy-01.txt'), 'b': resource('run-vaswani-dummy-02.txt'), })[:1])
