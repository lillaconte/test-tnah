import pytest
from src.utils.utils import fetch_text

@pytest.mark.parametrize(
        "url, expected", [
                         ("https://example.com", "Example Domain"),
                         ("https://google.com", "Google")
        ]
                         )
def test_fetch_text(url, expected):
    assert expected in fetch_text(url)


@pytest.mark.parametrize(
        "url, error", [
            ("not_url", ValueError)
        ]
)

def text_fail_fetch_text(url, error):
    with pytest.raises(ValueError):
        fetch_text("not_url")
    with pytest.raises(ValueError):
        fetch_text(12)
    with pytest.raises(Exception):
        fetch_text("https://fake-url.net")

    url = "example.com"
    text = fetch_text(url)
    assert "Example Domain" in text
