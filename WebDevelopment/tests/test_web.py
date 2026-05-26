"""Tests for the WebDevelopment learning guide."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
WEB = REPO_ROOT / "WebDevelopment"


def test_single_web_readme():
    md_files = list(WEB.rglob("*.md"))
    assert md_files == [WEB / "README.md"]


def test_readme_beginner_friendly():
    text = (WEB / "README.md").read_text()
    assert "Start here" in text
    assert "Who is this for" in text
    assert "Introduction.html" in text
    assert "Progress markers" in text
    for marker in ("[ ]", "[~]", "[x]"):
        assert marker in text


def test_html_examples_exist():
    assert (WEB / "HTML/Introduction.html").is_file()
    assert (WEB / "HTML/Example-1.html").is_file()


def test_react_and_node_exist():
    assert (WEB / "React/src/App.js").is_file()
    assert (WEB / "Node/app.js").is_file()
