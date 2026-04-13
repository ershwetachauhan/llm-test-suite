import pytest
from conftest import ask_gemini

def test_handles_greeting(model):
    """Model should respond gracefully to a simple greeting."""
    response = ask_gemini(model, "Hi")
    assert len(response.strip()) > 0

def test_handles_long_input(model):
    """Model should handle a long repetitive input without crashing."""
    long_prompt = "Tell me something interesting about space. " * 40
    response = ask_gemini(model, long_prompt)
    assert len(response) > 0

def test_multilingual_prompt(model):
    """Model should respond in French when asked."""
    response = ask_gemini(model, "Réponds uniquement en français. De quelle couleur est le ciel?")
    french_clues = ["ciel", "bleu", "est", "couleur", "le"]
    assert any(word in response.lower() for word in french_clues), \
        f"Expected French response, got: {response}"

def test_handles_nonsense_input(model):
    """Model should handle garbled input without crashing."""
    response = ask_gemini(model, "asdkfjhaskdjfh bbbbb 123 ???")
    assert len(response.strip()) > 0