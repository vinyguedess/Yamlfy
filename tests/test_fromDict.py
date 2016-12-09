from unittest import TestCase
from Yamlfy import FromDict


class TestFromDict(TestCase):

    def test_from_dict(self):

        yaml = FromDict({
            'name': 'Vinicius Guedes',
            'age': 29,
            'last_experiente': {
                'company': 'Grupo Ideal Trends',
                'job_title': 'Software development coordinator',
                'period': {
                    'start': '2016-01',
                    'end': None,
                    'current': True
                }
            }
        })

        self.assertIsInstance(yaml.get_yaml(), str)
