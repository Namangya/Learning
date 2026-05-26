-- User creation
-- CREATE USER username IDENTIFIED BY password;

-- Role assignment
-- GRANT CONNECT, RESOURCE TO username;
-- GRANT dba TO username;  -- use sparingly

-- Privilege grants
-- GRANT SELECT ON schema.table TO username;
-- REVOKE SELECT ON schema.table FROM username;

-- Auditing
-- AUDIT SELECT TABLE BY username;
-- Unified Auditing (12c+): CREATE AUDIT POLICY
