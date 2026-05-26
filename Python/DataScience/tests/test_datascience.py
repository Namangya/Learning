"""Tests for the Python DataScience track (lesson files and content)."""

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
DS = REPO_ROOT / "Python" / "DataScience"
PYTHON_README = REPO_ROOT / "Python" / "README.md"


def test_datascience_folder_exists():
    assert DS.is_dir()


def test_numpy_starter_content():
    text = (DS / "01_NumPy/numpy_starter.py").read_text()
    assert "import numpy" in text
    assert "array operations" in text.lower() or "Array Operations" in text


def test_pandas_starter_content():
    text = (DS / "02_Pandas/pandas_starter.py").read_text()
    for token in ("DataFrame", "read_csv", "groupby", "fillna"):
        assert token in text


def test_visualization_starter_content():
    text = (DS / "03_Visualization/visualization_starter.py").read_text()
    assert "matplotlib" in text and "seaborn" in text


def test_statistics_starter_content():
    text = (DS / "04_Statistics/statistics_starter.py").read_text()
    assert "scipy" in text
    assert "hypothesis" in text.lower()


def test_ml_starter_content():
    text = (DS / "05_MachineLearning/ml_starter.py").read_text()
    for token in ("train_test_split", "Pipeline", "fit", "score"):
        assert token in text


def test_projects_subdirs():
    subdirs = [p for p in (DS / "06_Projects").iterdir() if p.is_dir()]
    assert len(subdirs) >= 2


def test_python_readme_covers_datascience():
    text = PYTHON_README.read_text()
    assert "DataScience" in text
    assert "Start here" in text
    assert "numpy_starter.py" in text
    for cmd in ("python -m venv", "pip install -r requirements.txt"):
        assert cmd in text


def test_no_extra_markdown_in_datascience():
    md_files = list(DS.rglob("*.md"))
    assert md_files == [], f"Remove extra guides: {md_files}"


def test_requirements_at_python_level():
    req = REPO_ROOT / "Python/requirements.txt"
    assert req.is_file()
    text = req.read_text()
    assert "numpy==" in text
    assert not (DS / "requirements.txt").exists()
