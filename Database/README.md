# Database

Learning materials for relational databases, schema versioning, and deployment tools.

---

## Structure

```
Database/
├── PostgreSQL/
│   ├── notes/                          # Commands, setup scripts, reference PDFs
│   └── projects/
│       └── online-shopping-cart/
│           ├── sql/                    # Plain SQL version (no schema prefix)
│           └── postgresql/             # PostgreSQL version (Learn. schema + changelogs)
│               └── changelog/          # Liquibase XML changelogs for this project
├── Liquibase/                          # Liquibase config + master changelogs
└── Firefly/                            # Firefly config + changelogs (mirrors Liquibase)
```

---

## PostgreSQL

**Notes** (`PostgreSQL/notes/`)

| File | What it covers |
|------|---------------|
| `PostgreSQL-Notes.pgsql` | Domains, config file location, start/stop commands |
| `PSQL_SQL_Commands.sql` | `psql` meta-commands (`\dt`, `\l`, `\d`, `\dn`, etc.) |
| `PostGres Ubuntu SetUp.sh` | Full Ubuntu install walkthrough |
| `Terminal Queries.bash` | Handy terminal one-liners |
| `GIT_Comands.sh` | Git commands reference |
| `my_script.sql` | Scratch SQL script |
| `*.pdf` | Reference PDFs (SQL commands, Git cheat sheet, MongoDB) |

**Project — Online Shopping Cart** (`PostgreSQL/projects/online-shopping-cart/`)

Two versions of the same e-commerce database schema:

| Folder | Description |
|--------|-------------|
| `sql/` | Plain SQL — no schema prefix, runs on any PostgreSQL database |
| `postgresql/` | PostgreSQL-specific — uses `Learn.` schema, includes Liquibase changelogs |

Files in each version:

| File | Purpose |
|------|---------|
| `Table.sql` / `ddl_for_tables.sql` | CREATE TABLE statements for all entities |
| `Insert.sql` / `insert_for_tables.sql` | 100 users + full seed data |
| `Modification.sql` | SELECT queries, UPDATE, DELETE, VIEWs, CHECK constraints |
| `ddl_for_schema.sql` | CREATE SCHEMA |
| `ddl_for_extension.sql` | PostGIS extension |
| `index.sql` / `ddl_for_index.sql` | Index definitions with usage comments |
| `storedprocedure.sql` | Stored function + trigger for audit logging |
| `changelog/` | Liquibase XML changesets (postgresql version only) |

---

## Liquibase

Schema version control tool. Tracks and deploys database changes via XML changesets.

| File | Purpose |
|------|---------|
| `liquibase.properties` | Default connection config |
| `liquibase_dev.properties` | Dev environment config |
| `changelog.xml` | Main changelog entry point |
| `master_changelog.xml` | Master changelog that includes others |
| `Liquibase_Commands.sh` | Common Liquibase CLI commands |

```bash
# Apply all pending changes
liquibase update

# Preview SQL without running
liquibase updateSQL

# Roll back last change
liquibase rollbackCount 1
```

---

## Firefly

Database deployment tool — same structure as Liquibase.

| File | Purpose |
|------|---------|
| `firefly.properties` | Connection + deployment config |
| `changelog.xml` | Changelog entry point |

```bash
# Deploy changes
firefly deploy

# Preview changes
firefly preview
```

---

## Resources

- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Liquibase Docs](https://docs.liquibase.com/)
- [pgAdmin](https://www.pgadmin.org/)
