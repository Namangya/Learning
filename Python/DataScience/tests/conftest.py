from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
DATASCIENCE = REPO_ROOT / "Python" / "DataScience"


@pytest.fixture
def ds_root():
    return DATASCIENCE
