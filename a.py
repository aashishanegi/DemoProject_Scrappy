import sqlite3

conn = sqlite3.connect('jobs.db')
c = conn.cursor()
c.execute("SELECT * FROM jobs")
jobs = c.fetchall()
for job in jobs:
    print(job)
conn.close()
