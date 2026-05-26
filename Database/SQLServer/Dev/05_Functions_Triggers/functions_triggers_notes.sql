-- SQLServer — 05 Functions Triggers
-- Scalar functions
-- Return a single value; used in SELECT expressions

-- Table-valued functions (TVF)
-- SQL Server supports inline and multi-statement table-valued functions (TVFs).
-- CREATE FUNCTION ... RETURNS TABLE AS RETURN (SELECT ...);

-- BEFORE/AFTER triggers
-- BEFORE: validate or modify row before write
-- AFTER: audit logging, cascading side effects

-- Trigger use cases
-- Audit trails, enforcing business rules, maintaining derived columns
