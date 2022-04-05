import unittest

from jqqb import QueryBuilder


class TestAdvancedRule(unittest.TestCase):
    def setUp(self):
        self.rule = {
            "condition": "OR",
            "rules": [
                {
                    "condition": "AND",
                    "rules": [
                        {
                            "rules": [
                                {
                                    "id": "assets.custom_fields.cible_traitement_semence",  # noqa: E501
                                    "type": "string",
                                    "field": "assets.custom_fields.cible_traitement_semence",  # noqa: E501
                                    "input": "text",
                                    "value": "cécidomyes, puceron",
                                    "operator": "in",
                                },
                                {
                                    "id": "assets.custom_fields.traitement_semence",  # noqa: E501
                                    "type": "integer",
                                    "field": "assets.custom_fields.traitement_semence",  # noqa: E501
                                    "input": "number",
                                    "value": 1,
                                    "operator": "equal",
                                },
                            ],
                            "valid": True,
                            "condition": "AND",
                        },
                        {
                            "rules": [
                                {
                                    "id": "assets.custom_fields.culture_lib",
                                    "type": "string",
                                    "field": "assets.custom_fields.culture_lib",
                                    "input": "text",
                                    "value": "ble tendre d'hiver",
                                    "operator": "equal",
                                }
                            ],
                            "valid": True,
                            "condition": "AND",
                        },
                        {
                            "rules": [
                                {
                                    "id": "assets.custom_fields.date_recolte",
                                    "type": "date",
                                    "field": "assets.custom_fields.date_recolte",  # noqa: E501
                                    "input": "text",
                                    "value": "2021-07-10",
                                    "operator": "greater_or_equal",
                                }
                            ],
                            "valid": True,
                            "condition": "AND",
                        },
                        {
                            "rules": [
                                {
                                    "id": "assets.custom_fields.densite_semis",
                                    "type": "double",
                                    "field": "assets.custom_fields.densite_semis",  # noqa: E501
                                    "input": "number",
                                    "value": [195, 300],
                                    "operator": "between",
                                }
                            ],
                            "valid": True,
                            "condition": "AND",
                        },
                        {
                            "rules": [
                                {
                                    "id": "assets.custom_fields.culture_precedente",  # noqa: E501
                                    "type": "string",
                                    "field": "assets.custom_fields.culture_precedente",  # noqa: E501
                                    "input": "text",
                                    "value": "Mais",
                                    "operator": "not_equal",
                                },
                                {
                                    "id": "assets.custom_fields.culture_precedente",  # noqa: E501
                                    "type": "string",
                                    "field": "assets.custom_fields.culture_precedente",  # noqa: E501
                                    "input": "text",
                                    "value": None,
                                    "operator": "is_not_null",
                                },
                            ],
                            "valid": True,
                            "condition": "AND",
                        },
                        {
                            "rules": [
                                {
                                    "id": "assets.custom_fields.objectif_rendement",  # noqa: E501
                                    "type": "double",
                                    "field": "assets.custom_fields.objectif_rendement",  # noqa: E501
                                    "input": "number",
                                    "value": 70,
                                    "operator": "greater_or_equal",
                                }
                            ],
                            "valid": True,
                            "condition": "AND",
                        },
                        {
                            "rules": [
                                {
                                    "id": "assets.location.postcode",
                                    "type": "string",
                                    "field": "assets.location.postcode",
                                    "input": "text",
                                    "value": "21",
                                    "operator": "begins_with",
                                },
                                {
                                    "id": "assets.location.postcode",
                                    "type": "string",
                                    "field": "assets.location.postcode",
                                    "input": "text",
                                    "value": "25",
                                    "operator": "begins_with",
                                },
                                {
                                    "id": "assets.location.postcode",
                                    "type": "string",
                                    "field": "assets.location.postcode",
                                    "input": "text",
                                    "value": "39",
                                    "operator": "begins_with",
                                },
                            ],
                            "valid": True,
                            "condition": "OR",
                        },
                        {
                            "rules": [
                                {
                                    "id": "assets.custom_fields.variety",
                                    "type": "string",
                                    "field": "assets.custom_fields.variety",
                                    "input": "text",
                                    "value": "Rimbaud, Descartes, Accor",
                                    "operator": "in",
                                },
                                {
                                    "id": "assets.custom_fields.traitement_semence",  # noqa: E501
                                    "type": "integer",
                                    "field": "assets.custom_fields.traitement_semence",  # noqa: E501
                                    "input": "number",
                                    "value": 1,
                                    "operator": "equal",
                                },
                            ],
                            "valid": True,
                            "condition": "AND",
                        },
                    ],
                },
                {
                    "condition": "OR",
                    "rules": [
                        {
                            "rules": [
                                {
                                    "id": "assets.custom_fields.culture_suivante",  # noqa: E501
                                    "type": "string",
                                    "field": "assets.custom_fields.culture_suivante",  # noqa: E501
                                    "input": "text",
                                    "value": "Blé dur, Pois, Rien",
                                    "operator": "in",
                                },
                                {
                                    "id": "assets.custom_fields.culture_suivante",  # noqa: E501
                                    "type": "string",
                                    "field": "assets.custom_fields.culture_suivante",  # noqa: E501
                                    "input": "text",
                                    "value": None,
                                    "operator": "is_not_null",
                                },
                            ],
                            "valid": True,
                            "condition": "OR",
                        },
                        {
                            "rules": [
                                {
                                    "rules": [
                                        {
                                            "id": "assets.custom_fields.type_sol",  # noqa: E501
                                            "type": "string",
                                            "field": "assets.custom_fields.type_sol",  # noqa: E501
                                            "input": "text",
                                            "value": "Limoneux",
                                            "operator": "equal",
                                        },
                                        {
                                            "id": "assets.custom_fields.tillage",  # noqa: E501
                                            "type": "integer",
                                            "field": "assets.custom_fields.tillage",  # noqa: E501
                                            "input": "number",
                                            "value": 1,
                                            "operator": "equal",
                                        },
                                    ],
                                    "condition": "AND",
                                },
                                {
                                    "rules": [
                                        {
                                            "id": "assets.custom_fields.type_sol",  # noqa: E501
                                            "type": "string",
                                            "field": "assets.custom_fields.type_sol",  # noqa: E501
                                            "input": "text",
                                            "value": "Limoneux",
                                            "operator": "not_equal",
                                        }
                                    ],
                                    "condition": "AND",
                                },
                            ],
                            "valid": True,
                            "condition": "OR",
                        },
                        {
                            "rules": [
                                {
                                    "id": "assets.custom_fields.type_sol",
                                    "type": "string",
                                    "field": "assets.custom_fields.type_sol",
                                    "input": "text",
                                    "value": None,
                                    "operator": "is_not_null",
                                },
                                {
                                    "id": "assets.custom_fields.type_sol",
                                    "type": "string",
                                    "field": "assets.custom_fields.type_sol",
                                    "input": "text",
                                    "value": "Argilo-calcaire superficiel, Argileux, Limoneux",  # noqa: E501
                                    "operator": "in",
                                },
                            ],
                            "valid": True,
                            "condition": "AND",
                        },
                    ],
                },
                {
                    "condition": "OR",
                    "rules": [
                        {
                            "rules": [
                                {
                                    "id": "assets.custom_fields.interculture",
                                    "type": "string",
                                    "field": "assets.custom_fields.interculture",  # noqa: E501
                                    "input": "text",
                                    "value": None,
                                    "operator": "is_not_null",
                                }
                            ],
                            "valid": True,
                            "condition": "AND",
                        },
                        {
                            "rules": [
                                {
                                    "id": "assets.custom_fields.surface_culture",  # noqa: E501
                                    "type": "double",
                                    "field": "assets.custom_fields.surface_culture",  # noqa: E501
                                    "input": "number",
                                    "value": None,
                                    "operator": "is_not_null",
                                }
                            ],
                            "valid": True,
                            "condition": "AND",
                        },
                    ],
                },
            ],
        }

        self.objects = [
            {
                "actor": {
                    "identification_number": "63778926410101",
                    "company_name": "USINE DES BONS PAINS",
                    "public_id": "391b79cd31ce53dbad388714386779d2b89a7ba0ab71312cc183678ad87dd28f32080128478692784c7ef706cba2d03be399d95a5f2cf7f20f541c273db7a8bf",  # noqa: E501
                    "name": "USINE DES BONS PAINS",
                    "description": "",
                    "activated": "2021-03-14 15:00:00+00:00",
                    "archived": "None",
                    "created": "2021-03-14 15:00:00+00:00",
                    "updated": "None",
                    "tags": ["Usine de panification"],
                    "custom_fields": {},
                },
                "assets": [
                    {
                        "public_id": "c558fabb9d3806c6160d66500b2a8e4df80a74660b940a37d5af2b4ea754774674a17d6de0a89dc79d3dedafe292e85aea42cf3570c19e4d30c5f2125f8fd5ca",  # noqa: E501
                        "name": "Ligne de conditionnement - U01 - L3",
                        "description": "",
                        "activated": "2021-03-14 15:00:00+00:00",
                        "archived": "None",
                        "created": "2021-03-14 15:00:00+00:00",
                        "updated": "None",
                        "tags": ["L3", "U01"],
                        "actor": "391b79cd31ce53dbad388714386779d2b89a7ba0ab71312cc183678ad87dd28f32080128478692784c7ef706cba2d03be399d95a5f2cf7f20f541c273db7a8bf",  # noqa: E501
                        "location": {
                            "public_id": "506fd24c1ae3fca41400d7182800631835de0b7d31e894bb667f3aa9ab71d0bcee82c328a78dafc07bf71423dd0c151293a4a98c76e98c2ceefaa40d69c2dd1f",  # noqa: E501
                            "name": "USINE DES BONS PAINS",
                            "description": "",
                            "activated": "2022-02-24 18:49:26.304000+00:00",
                            "archived": "None",
                            "created": "2021-03-14 15:00:00+00:00",
                            "updated": "2022-02-24 18:49:26.452000+00:00",
                            "tags": [
                                "Usine",
                                "U01",
                                "L2",
                                "L3",
                                "ZE_02",
                                "ZP_01",
                                "ZR_04",
                            ],
                            "actor": "391b79cd31ce53dbad388714386779d2b89a7ba0ab71312cc183678ad87dd28f32080128478692784c7ef706cba2d03be399d95a5f2cf7f20f541c273db7a8bf",  # noqa: E501
                            "first_name": "",
                            "last_name": "",
                            "company_name": "USINE DES BONS PAINS",
                            "line_1": "Route de Dole",
                            "line_2": "",
                            "line_3": "",
                            "postcode": "39100",
                            "country": "FR",
                            "city": "Dole",
                            "gln": "",
                            "custom_fields": {"internal_code": "U01"},
                        },
                        "category": 3,
                        "capacity": 0.0,
                        "giai": "",
                        "custom_fields": {
                            "tool_type": "production",
                            "internal_code": "L3",
                            "site_internal_code": "U01",
                        },
                    },
                    {
                        "public_id": "faf6add304d20a88479c76d50f91a63b7706a177db80e45355e8ee7c0a72d42db1947bcee4886f1a877c5ba2031234825e826d64fa94151e32dd8e51e0d92269",  # noqa: E501
                        "name": "Ligne de transformation - U01 - L2",
                        "description": "",
                        "activated": "2021-03-14 15:00:00+00:00",
                        "archived": "None",
                        "created": "2021-03-14 15:00:00+00:00",
                        "updated": "None",
                        "tags": ["L2", "U01"],
                        "actor": "391b79cd31ce53dbad388714386779d2b89a7ba0ab71312cc183678ad87dd28f32080128478692784c7ef706cba2d03be399d95a5f2cf7f20f541c273db7a8bf",  # noqa: E501
                        "location": {
                            "public_id": "506fd24c1ae3fca41400d7182800631835de0b7d31e894bb667f3aa9ab71d0bcee82c328a78dafc07bf71423dd0c151293a4a98c76e98c2ceefaa40d69c2dd1f",  # noqa: E501
                            "name": "USINE DES BONS PAINS",
                            "description": "",
                            "activated": "2022-02-24 18:49:26.304000+00:00",
                            "archived": "None",
                            "created": "2021-03-14 15:00:00+00:00",
                            "updated": "2022-02-24 18:49:26.452000+00:00",
                            "tags": [
                                "Usine",
                                "U01",
                                "L2",
                                "L3",
                                "ZE_02",
                                "ZP_01",
                                "ZR_04",
                            ],
                            "actor": "391b79cd31ce53dbad388714386779d2b89a7ba0ab71312cc183678ad87dd28f32080128478692784c7ef706cba2d03be399d95a5f2cf7f20f541c273db7a8bf",  # noqa: E501
                            "first_name": "",
                            "last_name": "",
                            "company_name": "USINE DES BONS PAINS",
                            "line_1": "Route de Dole",
                            "line_2": "",
                            "line_3": "",
                            "postcode": "39100",
                            "country": "FR",
                            "city": "Dole",
                            "gln": "",
                            "custom_fields": {"internal_code": "U01"},
                        },
                        "category": 3,
                        "capacity": 0.0,
                        "giai": "",
                        "custom_fields": {
                            "tool_type": "production",
                            "internal_code": "L2",
                            "site_internal_code": "U01",
                        },
                    },
                    {
                        "public_id": "eeef9b80939a14edd6c80917e338aeb9e312054d0b7c1326560ff538742c0b966244cae7cfbdf5f05c835ef5db802def0db568b36734ea3ae1f992f7b51eb073",  # noqa: E501
                        "name": "Zone attente ensachage - U01 - ZE_02",
                        "description": "",
                        "activated": "2021-03-14 15:00:00+00:00",
                        "archived": "None",
                        "created": "2021-03-14 15:00:00+00:00",
                        "updated": "None",
                        "tags": ["ZE_02", "U01"],
                        "actor": "391b79cd31ce53dbad388714386779d2b89a7ba0ab71312cc183678ad87dd28f32080128478692784c7ef706cba2d03be399d95a5f2cf7f20f541c273db7a8bf",  # noqa: E501
                        "location": {
                            "public_id": "506fd24c1ae3fca41400d7182800631835de0b7d31e894bb667f3aa9ab71d0bcee82c328a78dafc07bf71423dd0c151293a4a98c76e98c2ceefaa40d69c2dd1f",  # noqa: E501
                            "name": "USINE DES BONS PAINS",
                            "description": "",
                            "activated": "2022-02-24 18:49:26.304000+00:00",
                            "archived": "None",
                            "created": "2021-03-14 15:00:00+00:00",
                            "updated": "2022-02-24 18:49:26.452000+00:00",
                            "tags": [
                                "Usine",
                                "U01",
                                "L2",
                                "L3",
                                "ZE_02",
                                "ZP_01",
                                "ZR_04",
                            ],
                            "actor": "391b79cd31ce53dbad388714386779d2b89a7ba0ab71312cc183678ad87dd28f32080128478692784c7ef706cba2d03be399d95a5f2cf7f20f541c273db7a8bf",  # noqa: E501
                            "first_name": "",
                            "last_name": "",
                            "company_name": "USINE DES BONS PAINS",
                            "line_1": "Route de Dole",
                            "line_2": "",
                            "line_3": "",
                            "postcode": "39100",
                            "country": "FR",
                            "city": "Dole",
                            "gln": "",
                            "custom_fields": {"internal_code": "U01"},
                        },
                        "category": 2,
                        "capacity": 0.0,
                        "giai": "",
                        "custom_fields": {
                            "tool_type": "stockage",
                            "internal_code": "ZE_02",
                            "site_internal_code": "U01",
                        },
                    },
                    {
                        "public_id": "6e984bbb523581886aaa4943f871b7949722243f16a8239b03337a3fa28f2631dab6487d461e76df3b6c039d7da8e2f8637cf7c52061d3eb2bff9fe93babd3ea",  # noqa: E501
                        "name": "Zone palette - U01 - ZP_01",
                        "description": "",
                        "activated": "2021-03-14 15:00:00+00:00",
                        "archived": "None",
                        "created": "2021-03-14 15:00:00+00:00",
                        "updated": "None",
                        "tags": ["ZP_01", "U01"],
                        "actor": "391b79cd31ce53dbad388714386779d2b89a7ba0ab71312cc183678ad87dd28f32080128478692784c7ef706cba2d03be399d95a5f2cf7f20f541c273db7a8bf",  # noqa: E501
                        "location": {
                            "public_id": "506fd24c1ae3fca41400d7182800631835de0b7d31e894bb667f3aa9ab71d0bcee82c328a78dafc07bf71423dd0c151293a4a98c76e98c2ceefaa40d69c2dd1f",  # noqa: E501
                            "name": "USINE DES BONS PAINS",
                            "description": "",
                            "activated": "2022-02-24 18:49:26.304000+00:00",
                            "archived": "None",
                            "created": "2021-03-14 15:00:00+00:00",
                            "updated": "2022-02-24 18:49:26.452000+00:00",
                            "tags": [
                                "Usine",
                                "U01",
                                "L2",
                                "L3",
                                "ZE_02",
                                "ZP_01",
                                "ZR_04",
                            ],
                            "actor": "391b79cd31ce53dbad388714386779d2b89a7ba0ab71312cc183678ad87dd28f32080128478692784c7ef706cba2d03be399d95a5f2cf7f20f541c273db7a8bf",  # noqa: E501
                            "first_name": "",
                            "last_name": "",
                            "company_name": "USINE DES BONS PAINS",
                            "line_1": "Route de Dole",
                            "line_2": "",
                            "line_3": "",
                            "postcode": "39100",
                            "country": "FR",
                            "city": "Dole",
                            "gln": "",
                            "custom_fields": {"internal_code": "U01"},
                        },
                        "category": 2,
                        "capacity": 0.0,
                        "giai": "",
                        "custom_fields": {
                            "tool_type": "stockage",
                            "internal_code": "ZP_01",
                            "site_internal_code": "U01",
                        },
                    },
                    {
                        "public_id": "c2887547082c5ada76fc2e8fcdb99341493c9fdcc882ed72bb558a897c6947b4d745234e59d40ddf51619cc6091de15d7859bbd8753c4eb0c953b2cf5e17609a",  # noqa: E501
                        "name": "Zone réception - U01 - ZR_04",
                        "description": "",
                        "activated": "2021-03-14 15:00:00+00:00",
                        "archived": "None",
                        "created": "2021-03-14 15:00:00+00:00",
                        "updated": "None",
                        "tags": ["ZR_04", "U01"],
                        "actor": "391b79cd31ce53dbad388714386779d2b89a7ba0ab71312cc183678ad87dd28f32080128478692784c7ef706cba2d03be399d95a5f2cf7f20f541c273db7a8bf",  # noqa: E501
                        "location": {
                            "public_id": "506fd24c1ae3fca41400d7182800631835de0b7d31e894bb667f3aa9ab71d0bcee82c328a78dafc07bf71423dd0c151293a4a98c76e98c2ceefaa40d69c2dd1f",  # noqa: E501
                            "name": "USINE DES BONS PAINS",
                            "description": "",
                            "activated": "2022-02-24 18:49:26.304000+00:00",
                            "archived": "None",
                            "created": "2021-03-14 15:00:00+00:00",
                            "updated": "2022-02-24 18:49:26.452000+00:00",
                            "tags": [
                                "Usine",
                                "U01",
                                "L2",
                                "L3",
                                "ZE_02",
                                "ZP_01",
                                "ZR_04",
                            ],
                            "actor": "391b79cd31ce53dbad388714386779d2b89a7ba0ab71312cc183678ad87dd28f32080128478692784c7ef706cba2d03be399d95a5f2cf7f20f541c273db7a8bf",  # noqa: E501
                            "first_name": "",
                            "last_name": "",
                            "company_name": "USINE DES BONS PAINS",
                            "line_1": "Route de Dole",
                            "line_2": "",
                            "line_3": "",
                            "postcode": "39100",
                            "country": "FR",
                            "city": "Dole",
                            "gln": "",
                            "custom_fields": {"internal_code": "U01"},
                        },
                        "category": 2,
                        "capacity": 0.0,
                        "giai": "",
                        "custom_fields": {
                            "tool_type": "stockage",
                            "internal_code": "ZR_04",
                            "site_internal_code": "U01",
                        },
                    },
                ],
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
        self.assertEqual(count, 1)
