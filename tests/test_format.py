import pytest
import json
from conftest import ask_gemini

def test_response_not_empty(model):
    """Model should always return a non-empty response."""
    response = ask_gemini(model, "Say hello.")
    assert len(response.strip()) > 0

def test_valid_json_output(model):
    """Model should return valid JSON when asked."""
    prompt = (
        'Return a JSON object with keys "name" and "age" for a fictional person. '
        'Return ONLY the raw JSON. No explanation, no markdown, no code fences.'
    )
    response = ask_gemini(model, prompt)
    # Strip any accidental markdown fences just in case
    clean = response.strip().strip("```json").strip("```").strip()
    try:
        data = json.loads(clean)
        assert "name" in data, "Missing 'name' key"
        assert "age" in data, "Missing 'age' key"
    except json.JSONDecodeError:
        pytest.fail(f"Response was not valid JSON: {response}")

def test_list_output(model):
    """Model should return a list when asked for one."""
    response = ask_gemini(model, "List exactly 3 colours, one per line. Nothing else.")
    lines = [line.strip() for line in response.strip().split("\n") if line.strip()]
    assert len(lines) >= 3, f"Expected 3 items, got: {lines}"

def test_short_answer_when_asked(model):
    """Model should respect a request for a brief answer."""
    response = ask_gemini(model, "What is the speed of light? Answer in one sentence maximum.")
    sentences = response.split(".")
    assert len(response) < 300, f"Response was too long: {response}"