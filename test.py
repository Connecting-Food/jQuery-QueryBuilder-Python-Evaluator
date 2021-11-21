import json
from jqqb import QueryBuilder


rule_json = {
    "condition": "AND",
    "rules": [
        {
            "id": "tagname",
            "field": "tags.name",
            "type": "string",
            "input": "text",
            "operator": "not_contains",
            "value": "production",
        },
        {
            "id": "tagname",
            "field": "tags.name",
            "type": "string",
            "input": "text",
            "operator": "begins_with",
            "value": "development",
        },
        {
            "condition": "OR",
            "rules": [
                {
                    "id": "type",
                    "field": "type",
                    "type": "string",
                    "input": "text",
                    "operator": "equal",
                    "value": "ec2",
                },
                {
                    "id": "type",
                    "field": "type",
                    "type": "string",
                    "input": "text",
                    "operator": "equal",
                    "value": "ami",
                },
            ],
        },
    ],
}

DIVIDER = "\n----\n"

query_builder = QueryBuilder(rule_json)
object_1 = {
    "type": "ec2",
    "tags": [{"name": "hello"}, {"name": "asdfasfproduction_instance"}],
}
object_2 = {
    "type": "ami",
    "tags": [
        {"name": "development"},
        {"name": "asfdafdroduction_instance"},
        {"name": "proction"},
    ],
}
objects = [object_1, object_2]

print(DIVIDER)

print(f"Parsed rule set:\n{query_builder.parsed_rule_set}")
print(DIVIDER)

print(f"Objects:\n{objects}")

print(DIVIDER)

print("Match objects:")
print(query_builder.match_objects(objects))
print(DIVIDER)

print("Inspect objects:")
print(json.dumps(query_builder.inspect_objects(objects)))
print(DIVIDER)
