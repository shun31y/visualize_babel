import sys

sys.path.append("..")
import json
import os

import Levenshtein
import pytest
import yaml

from src.model.chat import chat, chat_template


def load_test_cases(filepath: str) -> list[str]:
    with open(filepath, "r", encoding="utf-8") as file:
        test_cases = yaml.safe_load(file)
    return test_cases


@pytest.fixture
def setup():
    def _setup(file_path: str):
        file_path = os.path.join(os.path.dirname(__file__), file_path)
        return load_test_cases(file_path)

    return _setup


def test_chat_template(setup):
    test_cases = setup("testcase_chat/test_chat_template.yml")
    for test_case in test_cases:
        user_message = test_case["input"]
        preprocessed = json.loads(test_case["preprocessed"])
        messages = chat_template(user_message)
        assert messages == preprocessed


def test_chat(setup):
    test_cases = setup("testcase_chat/test_chat.yml")
    for test_case in test_cases:
        user_message = test_case["input"]
        correct = test_case["output"]
        output = chat(user_message)
        assert (
            float(
                Levenshtein.distance(output, correct)
                / (max(len(output), len(correct)) * 1.00)
            )
            <= 0.5
        )
