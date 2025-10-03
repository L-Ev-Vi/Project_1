import json
import os

import pytest

from src.utils import from_json_to_list


def test_from_json_to_list_not_file():
    assert from_json_to_list("file") == []


def test_from_json_to_list_not_value():
    n = {}
    with open("../data/test_file.json", "w", encoding="UTF-8") as f:
        json.dump(n, f)
    assert from_json_to_list("test_file") == []
    os.remove("../data/test_file.json")


def test_from_json_to_list_empty():
    n = []
    with open("../data/test_file.json", "w", encoding="UTF-8") as f:
        json.dump(n, f)
    assert from_json_to_list("test_file") == []
    os.remove("../data/test_file.json")


def test_from_json_to_list(list_json):
    for n in list_json:
        assert n in from_json_to_list("operations.json")
