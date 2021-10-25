import unittest
from mindsdb_native import F
from common import break_dataset


class TestBigQuery(unittest.TestCase):
    def test_bigquery_ds(self):
        from mindsdb_datasources import BigQueryDS

        LIMIT = 100

        query = """
            SELECT corpus AS title, COUNT(word) AS unique_words
            FROM `bigquery-public-data.samples.shakespeare`
            GROUP BY title
            ORDER BY unique_words
            DESC LIMIT {}
        """.format(LIMIT)

        bigquery_ds = BigQueryDS(
            query=query
        )

        bigquery_ds.df = break_dataset(bigquery_ds.df)

        assert len(bigquery_ds) == LIMIT

        F.analyse_dataset(bigquery_ds)