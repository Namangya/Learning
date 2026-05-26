-- AWR (Automatic Workload Repository) and ASH (Active Session History)

-- AWR Snapshot — manual snapshot
EXEC DBMS_WORKLOAD_REPOSITORY.CREATE_SNAPSHOT();

-- AWR Report — HTML report between two snapshot IDs
SELECT * FROM TABLE(DBMS_WORKLOAD_REPOSITORY.AWR_REPORT_HTML(
    l_dbid => (SELECT dbid FROM v$database),
    l_inst_num => 1,
    l_bid => <begin_snap_id>,
    l_eid => <end_snap_id>
));

-- ASH Report — recent active session history
SELECT * FROM TABLE(DBMS_WORKLOAD_REPOSITORY.ASH_REPORT_HTML(
    l_dbid => (SELECT dbid FROM v$database),
    l_inst_num => 1,
    l_btime => SYSDATE - 1/24,
    l_etime => SYSDATE
));
