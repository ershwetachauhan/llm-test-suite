import pytest
from conftest import ask_gemini

def test_capital_of_france(model):
    """Gemini should know basic geography."""
    response = ask_gemini(model, "What is the capital of France? Answer in one word only.")
    assert "Paris" in response

def test_simple_math(model):
    """Gemini should handle basic arithmetic."""
    response = ask_gemini(model, "What is 15 multiplied by 6? Reply with just the number.")
    assert "90" in response

def test_knows_planet_order(model):
    """Gemini should know basic science facts."""
    response = ask_gemini(model, "What is the closest planet to the Sun? One word answer.")
    assert "Mercury" in response

def test_historical_fact(model):
    """Gemini should know well-established history."""
    response = ask_gemini(model, "In what year did World War 2 end? Reply with just the year.")
    assert "1945" in response