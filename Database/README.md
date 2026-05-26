# Database — Learning Guide

This folder teaches **SQL databases** — how to design tables, write queries, and (for some paths) administer servers.

**Read this file only** — all setup, curricula, and dialect comparisons are here.

---

## Who is this for?

| Path | You want to… | Start in section |
|------|--------------|------------------|
| **SQL Developer** | Build apps that store data in tables | Pick a database below → **Dev curriculum** |
| **DBA** | Install, secure, back up, and tune databases | PostgreSQL or PL/SQL → **DBA curriculum** |
| **Comparing databases** | See how PostgreSQL vs MySQL vs Oracle differ | **Cross-dialect comparisons** (bottom half of this file) |

---

## Start here (pick ONE database)

Most beginners should start with **PostgreSQL** (free, widely used, good documentation).

| Database | First file to open | Role |
|----------|-------------------|------|
| **PostgreSQL** | `PostgreSQL/Dev/01_Schema_Design/schema_design_notes.sql` | Developer |
| **PostgreSQL (DBA)** | `PostgreSQL/DBA/01_Installation_Config/installation_notes.sql` | Administrator |
| **MySQL** | `MySQL/notes/MySQL_Notes.sql` | Developer |
| **Oracle SQL** | `OracleSQL/notes/OracleSQL_Notes.sql` | Developer |
| **PL/SQL** | `PLSQL/notes/PLSQL_Notes.sql` | Developer + Oracle DBA |
| **SQL Server** | `SQLServer/notes/SQLServer_Notes.sql` | Developer |

Open `.sql` files in any SQL editor, or run them in your database’s command tool (`psql`, MySQL Workbench, etc.).

---

## Progress markers

| Symbol | Meaning |
|--------|---------|
| `[ ]` | Not started |
| `[~]` | In progress |
| `[x]` | Done |

---

## Simple glossary

| Word | Meaning |
|------|---------|
| **SQL** | Language to ask questions of a database (`SELECT`, `INSERT`, …) |
| **Table** | Like a spreadsheet with rows and columns |
| **Dev track** | Writing queries and designing schemas for applications |
| **DBA track** | Keeping the database server healthy and secure |
| **Dialect** | Same SQL idea, slightly different syntax per vendor |

---

## Folder structure

```
Database/
├── PostgreSQL/   Dev + DBA · notes · projects
├── MySQL/        Dev · notes · projects
├── OracleSQL/    Dev · notes · projects
├── PLSQL/        Dev + DBA (Oracle) · notes · projects
├── SQLServer/    Dev · notes · projects
├── Liquibase/    Schema version control
└── Firefly/      Deployment tool
```

---

## PostgreSQL (15+)

**Where to start:** Developers → `PostgreSQL/Dev/01_Schema_Design/schema_design_notes.sql` · DBAs → `PostgreSQL/DBA/01_Installation_Config/installation_notes.sql`

**Setup (macOS):** `brew install postgresql@16 && brew services start postgresql@16`  
**Setup (Ubuntu):** `sudo apt install postgresql postgresql-contrib && sudo systemctl start postgresql`

**Connection:** `postgresql://<username>:<password>@localhost:5432/<database>`  
**Verify:** `SELECT version();`

### Dev curriculum

| # | Topic | Path | Status |
|---|-------|------|--------|
| 01 | Schema Design | `Dev/01_Schema_Design/` | [ ] |
| 02 | DDL | `Dev/02_DDL/` | [ ] |
| 03 | DML | `Dev/03_DML/` | [ ] |
| 04 | Stored Procedures | `Dev/04_Stored_Procedures/` | [ ] |
| 05 | Functions & Triggers | `Dev/05_Functions_Triggers/` | [ ] |
| 06 | Query Optimization | `Dev/06_Query_Optimization/` | [ ] |

### DBA curriculum

| # | Topic | Path | Status |
|---|-------|------|--------|
| 01 | Installation & Config | `DBA/01_Installation_Config/` | [ ] |
| 02 | User & Security | `DBA/02_User_Security/` | [ ] |
| 03 | Backup & Recovery | `DBA/03_Backup_Recovery/` | [ ] |
| 04 | Performance Tuning | `DBA/04_Performance_Tuning/` | [ ] |
| 05 | Monitoring | `DBA/05_Monitoring/` | [ ] |

### Notes (`PostgreSQL/notes/`)

`PostgreSQL-Notes.pgsql` · `PSQL_SQL_Commands.sql` · `PostGres Ubuntu SetUp.sh` · `Terminal Queries.bash`

### Projects

| Project | Path | Description |
|---------|------|-------------|
| Online Shopping Cart | `projects/online-shopping-cart/` | E-commerce schema (`sql/` plain, `postgresql/` with Learn. schema + Liquibase) |
| Library Catalog | `projects/library_catalog/schema.sql` | Books, members, loans |

---

## MySQL (8.0+)

**Where to start:** `MySQL/notes/MySQL_Notes.sql` → `MySQL/Dev/01_Schema_Design/`

**Setup:** `brew install mysql` (macOS) · `sudo apt install mysql-server` (Ubuntu)

**Connection:** `mysql://<username>:<password>@localhost:3306/<database>`

### Dev curriculum

| # | Topic | Path | Status |
|---|-------|------|--------|
| 01 | Schema Design | `MySQL/Dev/01_Schema_Design/` | [ ] |
| 02 | DDL | `MySQL/Dev/02_DDL/` | [ ] |
| 03 | DML | `MySQL/Dev/03_DML/` | [ ] |
| 04 | Stored Procedures | `MySQL/Dev/04_Stored_Procedures/` | [ ] |
| 05 | Functions & Triggers | `MySQL/Dev/05_Functions_Triggers/` | [ ] |
| 06 | Query Optimization | `MySQL/Dev/06_Query_Optimization/` | [ ] |

**License:** Community (free) · Enterprise (commercial)

### Projects

`projects/library_catalog/schema.sql` — library schema stub

---

## Oracle SQL (21c XE / 19c)

**Where to start:** `OracleSQL/notes/OracleSQL_Notes.sql` → `OracleSQL/Dev/01_Schema_Design/`

**Docker:**
```bash
docker pull container-registry.oracle.com/database/express:21.3.0-xe
docker run -d --name oracle-xe -p 1521:1521 -e ORACLE_PWD=<password> \
  container-registry.oracle.com/database/express:21.3.0-xe
```

**Connection:** `oracle://<username>:<password>@localhost:1521/XEPDB1`

### Dev curriculum

| # | Topic | Path | Status |
|---|-------|------|--------|
| 01 | Schema Design | `OracleSQL/Dev/01_Schema_Design/` | [ ] |
| 02 | DDL | `OracleSQL/Dev/02_DDL/` | [ ] |
| 03 | DML | `OracleSQL/Dev/03_DML/` | [ ] |
| 04 | Stored Procedures | `OracleSQL/Dev/04_Stored_Procedures/` | [ ] |
| 05 | Functions & Triggers | `OracleSQL/Dev/05_Functions_Triggers/` | [ ] |
| 06 | Query Optimization | `OracleSQL/Dev/06_Query_Optimization/` | [ ] |

**License:** XE (free dev) · Standard/Enterprise (production)

---

## PL/SQL (Oracle 21c XE / 19c)

**Where to start:** `PLSQL/notes/PLSQL_Notes.sql` → `PLSQL/Dev/01_Schema_Design/` · DBA → `PLSQL/DBA/01_Installation_Config/`

Same Docker setup as Oracle SQL. **Instant Client** needed for SQL*Plus / cx_Oracle.

**Connection:** `oracle://<username>:<password>@localhost:1521/XEPDB1`

### Dev curriculum

| # | Topic | Path | Status |
|---|-------|------|--------|
| 01 | Schema Design | `PLSQL/Dev/01_Schema_Design/` | [ ] |
| 02 | DDL | `PLSQL/Dev/02_DDL/` | [ ] |
| 03 | DML | `PLSQL/Dev/03_DML/` | [ ] |
| 04 | Stored Procedures | `PLSQL/Dev/04_Stored_Procedures/` | [ ] |
| 05 | Functions & Triggers | `PLSQL/Dev/05_Functions_Triggers/` | [ ] |
| 06 | Query Optimization | `PLSQL/Dev/06_Query_Optimization/` | [ ] |

### DBA curriculum (+ Oracle-specific)

| # | Topic | Path | Status |
|---|-------|------|--------|
| 01 | Installation & Config | `PLSQL/DBA/01_Installation_Config/` | [ ] |
| 02 | User & Security | `PLSQL/DBA/02_User_Security/` | [ ] |
| 03 | Backup & Recovery | `PLSQL/DBA/03_Backup_Recovery/` | [ ] |
| 04 | Performance Tuning | `PLSQL/DBA/04_Performance_Tuning/` | [ ] |
| 05 | Monitoring | `PLSQL/DBA/05_Monitoring/` | [ ] |
| 06 | Oracle Specific | `PLSQL/DBA/06_Oracle_Specific/` | [ ] |

Oracle DBA extras: `rman_backup.sh`, `v_views_notes.sql`, `awr_ash_notes.sql`, tablespace/undo/Data Guard/init.ora notes.

**License:** XE (free dev) · Enterprise (RMAN, Data Guard, AWR)

---

## SQL Server (2019+)

**Where to start:** `SQLServer/notes/SQLServer_Notes.sql` → `SQLServer/Dev/01_Schema_Design/`

**Docker:** `docker pull mcr.microsoft.com/mssql/server:2022-latest`

**Connection:** `mssql+pyodbc://<username>:<password>@localhost:1433/<database>?driver=ODBC+Driver+18+for+SQL+Server`

### Dev curriculum

| # | Topic | Path | Status |
|---|-------|------|--------|
| 01 | Schema Design | `SQLServer/Dev/01_Schema_Design/` | [ ] |
| 02 | DDL | `SQLServer/Dev/02_DDL/` | [ ] |
| 03 | DML | `SQLServer/Dev/03_DML/` | [ ] |
| 04 | Stored Procedures | `SQLServer/Dev/04_Stored_Procedures/` | [ ] |
| 05 | Functions & Triggers | `SQLServer/Dev/05_Functions_Triggers/` | [ ] |
| 06 | Query Optimization | `SQLServer/Dev/06_Query_Optimization/` | [ ] |

**License:** Developer (free) · Express (free, 10 GB limit) · Standard/Enterprise (production)

---

## Cross-dialect comparisons

# DDL Comparison

## CREATE TABLE

### PostgreSQL
```sql
CREATE TABLE t (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL);
```

### MySQL
```sql
CREATE TABLE t (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL);
```

### Oracle SQL / PL/SQL
```sql
CREATE TABLE t (id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, name VARCHAR2(100) NOT NULL);
```

### SQL Server
```sql
CREATE TABLE t (id INT IDENTITY(1,1) PRIMARY KEY, name NVARCHAR(100) NOT NULL);
```

## ALTER TABLE

### PostgreSQL
```sql
ALTER TABLE t ADD COLUMN email VARCHAR(255);
ALTER TABLE t DROP COLUMN email;
```

### MySQL
```sql
ALTER TABLE t ADD COLUMN email VARCHAR(255);
ALTER TABLE t DROP COLUMN email;
```

### Oracle SQL / PL/SQL
```sql
ALTER TABLE t ADD (email VARCHAR2(255));
ALTER TABLE t DROP COLUMN email;
```

### SQL Server
```sql
ALTER TABLE t ADD email NVARCHAR(255);
ALTER TABLE t DROP COLUMN email;
```

## DROP TABLE

All dialects: `DROP TABLE t;` (add `CASCADE` in PostgreSQL for dependent objects).

## Constraints

| Constraint | PostgreSQL | MySQL | Oracle | SQL Server |
|------------|-----------|-------|--------|------------|
| PRIMARY KEY | `PRIMARY KEY` | `PRIMARY KEY` | `PRIMARY KEY` | `PRIMARY KEY` |
| FOREIGN KEY | `REFERENCES t2(id)` | `REFERENCES t2(id)` | `REFERENCES t2(id)` | `REFERENCES t2(id)` |
| NOT NULL | `NOT NULL` | `NOT NULL` | `NOT NULL` | `NOT NULL` |
| UNIQUE | `UNIQUE` | `UNIQUE` | `UNIQUE` | `UNIQUE` |
| CHECK | `CHECK (col > 0)` | `CHECK (col > 0)` | `CHECK (col > 0)` | `CHECK (col > 0)` |


# Stored Procedures Comparison

## Procedure creation

### PostgreSQL
```sql
CREATE OR REPLACE PROCEDURE add_user(p_name TEXT)
LANGUAGE plpgsql AS $$
BEGIN
  INSERT INTO users(name) VALUES (p_name);
END; $$;
```

### MySQL
```sql
DELIMITER //
CREATE PROCEDURE add_user(IN p_name VARCHAR(100))
BEGIN
  INSERT INTO users(name) VALUES (p_name);
END //
DELIMITER ;
```

### Oracle SQL / PL/SQL
```sql
CREATE OR REPLACE PROCEDURE add_user(p_name IN VARCHAR2) AS
BEGIN
  INSERT INTO users(name) VALUES (p_name);
END;
/
```

### SQL Server
```sql
CREATE PROCEDURE add_user @p_name NVARCHAR(100)
AS
BEGIN
  INSERT INTO users(name) VALUES (@p_name);
END;
```

## Parameter declaration

| Dialect | Syntax |
|---------|--------|
| PostgreSQL | `p_name TEXT` (IN only until v14; INOUT in v14+) |
| MySQL | `IN p_name VARCHAR(100)`, `OUT`, `INOUT` |
| Oracle/PL/SQL | `p_name IN VARCHAR2`, `OUT`, `IN OUT` |
| SQL Server | `@p_name NVARCHAR(100)` (default IN), `@out INT OUTPUT` |

## Return value

| Dialect | Mechanism |
|---------|-----------|
| PostgreSQL | `OUT` parameters or `RETURNS` for functions |
| MySQL | `OUT`/`INOUT` parameters |
| Oracle/PL/SQL | `OUT`/`IN OUT`; functions use `RETURN` |
| SQL Server | `RETURN int` or `OUTPUT` parameters |

## Call / execute

| Dialect | Example |
|---------|---------|
| PostgreSQL | `CALL add_user('Alice');` |
| MySQL | `CALL add_user('Alice');` |
| Oracle/PL/SQL | `EXEC add_user('Alice');` or `BEGIN add_user('Alice'); END;` |
| SQL Server | `EXEC add_user @p_name = N'Alice';` |


# Data Types Comparison

| Category | PostgreSQL | MySQL | Oracle SQL | PL/SQL | SQL Server |
|----------|-----------|-------|------------|--------|------------|
| Integer | `SMALLINT`, `INTEGER`, `BIGINT` | `TINYINT`, `SMALLINT`, `INT`, `BIGINT` | `NUMBER(5)`, `NUMBER(10)`, `NUMBER(19)` | `NUMBER` | `TINYINT`, `SMALLINT`, `INT`, `BIGINT` |
| Decimal | `NUMERIC(p,s)`, `DECIMAL(p,s)` | `DECIMAL(p,s)` | `NUMBER(p,s)` | `NUMBER(p,s)` | `DECIMAL(p,s)`, `NUMERIC(p,s)` |
| Varchar | `VARCHAR(n)` | `VARCHAR(n)` | `VARCHAR2(n)` | `VARCHAR2(n)` | `VARCHAR(n)`, `NVARCHAR(n)` |
| Text | `TEXT` | `TEXT`, `LONGTEXT` | `CLOB` | `CLOB` | `VARCHAR(MAX)`, `NVARCHAR(MAX)` |
| Boolean | `BOOLEAN` | `TINYINT(1)` / `BOOL` | `NUMBER(1)` | `BOOLEAN` (23c+) | `BIT` |
| Date | `DATE` | `DATE` | `DATE` | `DATE` | `DATE` |
| Timestamp | `TIMESTAMP`, `TIMESTAMPTZ` | `DATETIME`, `TIMESTAMP` | `TIMESTAMP` | `TIMESTAMP` | `DATETIME2`, `DATETIMEOFFSET` |
| Binary/Blob | `BYTEA` | `BLOB`, `BINARY(n)` | `BLOB`, `RAW(n)` | `BLOB`, `RAW` | `VARBINARY(n)`, `VARBINARY(MAX)` |


### Primary use cases

| Dialect | Best for |
|---------|----------|
| PostgreSQL | Open-source apps, GIS (PostGIS), JSON |
| MySQL | Web apps (LAMP), WordPress |
| Oracle SQL | Enterprise ERP, banking, OLTP |
| PL/SQL | Oracle app logic, enterprise procedures |
| SQL Server | Microsoft stack (.NET), BI (SSRS) |

---

## Liquibase

| File | Purpose |
|------|---------|
| `liquibase.properties` | Connection config |
| `changelog.xml` | Entry point |
| `Liquibase_Commands.sh` | CLI reference |

```bash
liquibase update          # apply changes
liquibase updateSQL       # preview SQL
liquibase rollbackCount 1 # rollback
```

---

## Firefly

`firefly.properties` · `changelog.xml` — `firefly deploy` / `firefly preview`

---

## Resources

[PostgreSQL Docs](https://www.postgresql.org/docs/) · [Liquibase Docs](https://docs.liquibase.com/) · [pgAdmin](https://www.pgadmin.org/)

---

## Optional: automated checks

Tests live in `Database/tests/`. They verify lesson folders and files exist — they do **not** need a live database.

**One-time setup** (from repo root `Learning/`):

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install pytest hypothesis
```

**Run:**

```bash
pytest Database/tests -q
```

`.venv/` and `.pytest_cache/` are in `.gitignore` — do not commit them.
