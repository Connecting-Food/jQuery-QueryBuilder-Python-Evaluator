import unittest

from jqqb import QueryBuilder


class TestSimpleRule(unittest.TestCase):

    def setUp(self):
        self.rule = {
            "rules": [
                {
                    "rules": [
                        {
                            "rules": [
                                {
                                    "id": "actor.custom_fields.certificate_contrat_bio_21_started",  # noqa: E501
                                    "type": "date",
                                    "field": "actor.custom_fields.certificate_contrat_bio_21_started",  # noqa: E501
                                    "input": "text",
                                    "value": None,
                                    "operator": "is_not_null",
                                }
                            ],
                            "valid": True,
                            "condition": "AND",
                        }
                    ],
                    "condition": "AND",
                },
                {"rules": [], "condition": "OR"},
                {"rules": [], "condition": "OR"},
            ],
            "condition": "OR",
        }

        self.objects = [
            {
                "actor": {
                    "identification_number": "63778926410101",
                    "company_name": "USINE DES BONS PAINS",
                    "public_id": "dc8a564284b25a28afe3d28492f052d98c5bc22ebb3c68395291d2f40f4172c2",  # noqa: E501
                    "name": "USINE DES BONS PAINS",
                    "description": "",
                    "activated": "2021-03-14 15:00:00+00:00",
                    "archived": "None",
                    "created": "2021-03-14 15:00:00+00:00",
                    "updated": "None",
                    "tags": [
                        "demo",
                        "pain de mie",
                        "PAIN DE MIE BIO LOCAL",
                        "Usine de panification",
                    ],
                    "custom_fields": {
                        "certificate_contrat_bio_21_started": True
                    }
                }
            }, {
                "actor": {
                    "identification_number": "08007965988431",
                    "company_name": "SOCIETE COOPERATIVE 2",
                    "public_id": "f6308136b6b6105aef1739f4bc5ad88c9a95d66ce7d0bd5c2f4651bceb4c24b4",  # noqa: E501
                    "name": "SOCIETE COOPERATIVE 2",
                    "description": "",
                    "activated": "2021-03-14 15:00:00+00:00",
                    "archived": "None",
                    "created": "2021-03-14 15:00:00+00:00",
                    "updated": "None",
                    "tags": [
                        "demo",
                        "pain de mie",
                        "PAIN DE MIE BIO LOCAL",
                        "Organisme stockeur",
                    ],
                }
            }
        ]

    def test_load_rule(self):
        query_builder = QueryBuilder(self.rule)
        self.assertIsInstance(query_builder, QueryBuilder)

    def test_match_objects(self):
        query_builder = QueryBuilder(self.rule)
        count = len(query_builder.match_objects(self.objects))
        self.assertEqual(count, 1)

    def test_inspect_objects(self):
        query_builder = QueryBuilder(self.rule)
        count = len(query_builder.inspect_objects(self.objects))
        self.assertEqual(count, 2)
