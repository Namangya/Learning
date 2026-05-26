"""Tests for the Database learning scaffold."""

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
DB = REPO_ROOT / "Database"

DIALECTS = ["PostgreSQL", "MySQL", "OracleSQL", "PLSQL", "SQLServer"]
NEW_DIALECTS = ["MySQL", "OracleSQL", "PLSQL", "SQLServer"]
DEV_TOPICS = [
    "01_Schema_Design",
    "02_DDL",
    "03_DML",
    "04_Stored_Procedures",
    "05_Functions_Triggers",
    "06_Query_Optimization",
]
DBA_TOPICS = [
    "01_Installation_Config",
    "02_User_Security",
    "03_Backup_Recovery",
    "04_Performance_Tuning",
    "05_Monitoring",
]

hypothesis = pytest.importorskip("hypothesis")
from hypothesis import given, strategies as st


@pytest.mark.parametrize("dialect", NEW_DIALECTS)
def test_new_dialect_dir_exists(dialect):
    assert (DB / dialect).is_dir()


def test_single_database_readme():
    assert (DB / "README.md").is_file()
    md_files = list(DB.rglob("*.md"))
    assert md_files == [DB / "README.md"], f"Extra markdown: {md_files}"
    assert not (DB / "Comparisons").exists()


def test_database_readme_beginner_friendly():
    text = (DB / "README.md").read_text()
    assert "Start here" in text
    assert "Who is this for" in text
    for dialect in DIALECTS:
        assert dialect in text
    for marker in ("[ ]", "[~]", "[x]"):
        assert marker in text
    assert "<username>" in text
    assert "brew install" in text
    assert "docker pull" in text


def test_database_readme_comparisons():
    text = (DB / "README.md").read_text()
    for section in ("CREATE TABLE", "Procedure creation", "Integer"):
        assert section in text


@pytest.mark.parametrize("dialect", ["PostgreSQL", "PLSQL"])
def test_backup_recovery_notes_sections(dialect):
    path = DB / dialect / "DBA/03_Backup_Recovery/backup_recovery_notes.sql"
    text = path.read_text()
    for section in ("Full backup", "Incremental backup", "PITR", "Restore"):
        assert section in text


def test_plsql_oracle_specific_file_count():
    assert len(list((DB / "PLSQL/DBA/06_Oracle_Specific").glob("*"))) == 5


@given(st.sampled_from(DIALECTS))
def test_dialect_has_notes_and_projects(dialect):
    assert (DB / dialect / "notes").is_dir()
    assert (DB / dialect / "projects").is_dir()


@given(st.sampled_from(DIALECTS))
def test_dev_six_topics(dialect):
    for topic in DEV_TOPICS:
        assert (DB / dialect / "Dev" / topic).is_dir()


DEV_PREFIX = {
    "01_Schema_Design": "schema_design",
    "02_DDL": "ddl",
    "03_DML": "dml",
    "04_Stored_Procedures": "stored_procedures",
    "05_Functions_Triggers": "functions_triggers",
    "06_Query_Optimization": "query_optimization",
}


@given(st.sampled_from(DIALECTS))
def test_dev_topic_files(dialect):
    for topic, prefix in DEV_PREFIX.items():
        d = DB / dialect / "Dev" / topic
        assert (d / f"{prefix}_notes.sql").is_file()
        assert (d / f"{prefix}_exercise.sql").is_file()
