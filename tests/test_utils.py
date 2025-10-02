import pytest
from src.utils import from_json_to_list


def test_from_json_to_list_not_file():
    assert from_json_to_list('file') == []
