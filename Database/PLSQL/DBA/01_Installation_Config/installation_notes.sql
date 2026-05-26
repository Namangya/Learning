-- Installation & Configuration (Oracle)

-- Oracle XE via Docker
-- docker pull container-registry.oracle.com/database/express:21.3.0-xe
-- docker run -d --name oracle-xe -p 1521:1521 -e ORACLE_PWD=<password> ...

-- Key files
-- init.ora / spfile — initialization parameters
-- listener.ora — network listener config
