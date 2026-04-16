import unittest
from scripts.etl_pipeline import extract, transform

class TestETL(unittest.TestCase):
    def test_extract_csv(self):
        data = extract('data/customers.json')
        self.assertIsInstance(data, list)

    def test_transform_normalizes_names(self):
        records = [{'name': '  alice  ', 'monthly_spend': '100'}]
        result = transform(records)
        self.assertEqual(result[0]['name'], 'Alice')
