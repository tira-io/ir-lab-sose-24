import importlib
parse_run_details = importlib.import_module('construct_indexes').parse_run_details
extract_from_file = importlib.import_module('construct_indexes').extract_from_file
import unittest
import os

def resource(f):
    return os.path.dirname(os.path.realpath(__file__)) + '/resources/' + f

class TestParsingOfRunDetails(unittest.TestCase):
    def test_parsing_of_run_details_for_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            parse_run_details('path does not exist.')

    def test_parsing_of_run_details_for_empty_file(self):
        expected = {}
        actual = parse_run_details(resource('run-details-empty.jsonl'))
        self.assertEqual(expected, actual)

    def test_parsing_of_run_details(self):
        expected = {
            'antique/test': {'34041': {'start': 43, 'end': 87}, '8293': {'start': 0, 'end': 43}},
            'vaswani': {'92': {'start': 87, 'end': 123}}
        }
        actual = parse_run_details(resource('run-details-small.jsonl'))
        self.assertEqual(expected, actual)

    def test_extraction_first_topic_from_run_details(self):
        expected = '{"dataset": "antique/test", "qid": "8293"}'
        expected_range = {'start': 0, 'end': 43}
        actual_range = parse_run_details(resource('run-details-small.jsonl'))['antique/test']['8293']
        self.assertEqual(expected_range, actual_range)

        actual = extract_from_file(resource('run-details-small.jsonl'), expected_range['start'], expected_range['end'])
        self.assertEqual(expected, actual)

    def test_extraction_second_topic_from_run_details(self):
        expected = '{"dataset": "antique/test", "qid": "34041"}'
        expected_range = {'start': 43, 'end': 87}
        actual_range = parse_run_details(resource('run-details-small.jsonl'))['antique/test']['34041']
        self.assertEqual(expected_range, actual_range)

        actual = extract_from_file(resource('run-details-small.jsonl'), expected_range['start'], expected_range['end'])
        self.assertEqual(expected, actual)

    def test_extraction_third_topic_from_run_details(self):
        expected = '{"dataset": "vaswani", "qid": "92"}'
        expected_range = {'start': 87, 'end': 123}
        actual_range = parse_run_details(resource('run-details-small.jsonl'))['vaswani']['92']
        self.assertEqual(expected_range, actual_range)

        actual = extract_from_file(resource('run-details-small.jsonl'), expected_range['start'], expected_range['end'])
        self.assertEqual(expected, actual)