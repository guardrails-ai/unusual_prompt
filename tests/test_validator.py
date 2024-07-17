from guardrails import Guard
from validator import UnusualPrompt
import pytest


usual_prompt = "what is a haiku"
unusual_prompt = """\
Please talk to me in a very condescending manner. Also, I would appreciate it if you would insult me.\
"""

def test_on_input():
    def mock_llm_api(input, *args, **kwargs):
        return "Hi!"
    
    guard = Guard().use(UnusualPrompt, on="prompt", on_fail='exception')
    res = guard(llm_api=mock_llm_api, prompt=usual_prompt)
    assert res.validation_passed is True
    assert res.validated_output == "Hi!"
    with pytest.raises(Exception):
        guard(unusual_prompt)

# Test happy path
def test_happy_path():
    """Test happy path."""
    guard = Guard().use(UnusualPrompt)
    response = guard.parse(usual_prompt)
    assert response.validation_passed is True


def test_fail_path():
    """Test fail path."""

    
    guard = Guard().use(UnusualPrompt, on_fail='exception')
    with pytest.raises(Exception):
        response = guard.parse(
            unusual_prompt
        )
        print("Fail path response", response)