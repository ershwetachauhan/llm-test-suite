# LLM Test Suite — Google Gemini

A Python-based test suite for evaluating the quality and behaviour of Large Language Models (LLMs), built using Google Gemini's free API and pytest.

---

## What this project tests

| Category | File | What it checks |
|---|---|---|
| Factual accuracy | `test_factual.py` | Does the model return correct, verifiable answers? |
| Safety | `test_safety.py` | Does the model refuse harmful or dangerous requests? |
| Output format | `test_format.py` | Does the model follow formatting instructions (JSON, lists, length)? |
| Edge cases | `test_edge_cases.py` | Does the model handle unusual or unexpected inputs gracefully? |
| Consistency | `test_consistency.py` | Does the model return the same answer when asked the same question twice? |

---

## Why these test categories matter

**Factual accuracy** is the most basic quality check for any AI system. A model that returns wrong answers to simple factual questions cannot be trusted in production.

**Safety testing** ensures the model's guardrails are working. Every production AI application must refuse harmful, illegal, or dangerous requests — and that behaviour needs to be verified, not assumed.

**Output format testing** matters because real applications depend on structured responses. If an app expects JSON and the model returns plain text, the whole system breaks.

**Edge case testing** probes the boundaries of the model's behaviour. Good QA never only tests the happy path — it tests what happens when inputs are weird, empty, very long, or in a different language.

**Consistency testing** checks that the model is reliable. LLMs are probabilistic by nature, but wildly different answers to identical questions signals a quality problem.

---

## Tech stack

- **Python 3.14.2
- **Google Gemini API** (free tier — `gemini-2.0-flash-lite`)
- **pytest** — test runner
- **pytest-html** — HTML report generation
- **python-dotenv** — secure API key management

---

## Project structure

llm-test-suite/
├── tests/
│   ├── test_factual.py
│   ├── test_safety.py
│   ├── test_format.py
│   ├── test_edge_cases.py
│   └── test_consistency.py
├── conftest.py
├── requirements.txt
├── .env              ← never committed to GitHub
├── .gitignore
└── README.md

---

## How to run this project locally

**1. Clone the repository**
git clone https://github.com/ershwetachauhan/llm-test-suite.git
cd llm-test-suite

**2. Create and activate a virtual environment**
python3 -m venv venv
source venv/bin/activate

**3. Install dependencies**
pip3 install -r requirements.txt


**4. Add your API key**

Get a free API key from [Google AI Studio](https://aistudio.google.com), then create a `.env` file:
GEMINI_API_KEY=your_api_key_here

**5. Run the tests**

# Run all tests
pytest tests/ -v

# Run a single test file
pytest tests/test_factual.py -v

# Generate an HTML report
pytest tests/ -v --html=report.html --self-contained-html

---

## Example test output
tests/test_factual.py::test_capital_of_france        PASSED
tests/test_factual.py::test_simple_math              PASSED
tests/test_factual.py::test_knows_planet_order       PASSED
tests/test_factual.py::test_historical_fact          PASSED
tests/test_safety.py::test_refuses_hacking_request   PASSED
tests/test_safety.py::test_refuses_dangerous_instructions PASSED
tests/test_format.py::test_response_not_empty        PASSED
tests/test_format.py::test_valid_json_output         PASSED

---

## Notes

- The free tier of the Gemini API has rate limits. A 10-second delay is added between API calls in `conftest.py` to avoid hitting them.
- Never commit your `.env` file — your API key should stay private.

---

## Author

[LinkedIn] (https://www.linkedin.com/in/shweta-chauhan-770a693b/) 
[GitHub]   (https://github.com/ershwetachauhan)
