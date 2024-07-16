import sqlite3

def initialize_database():
    try:
        conn = sqlite3.connect('jobs.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS jobs
                     (id INTEGER PRIMARY KEY, title TEXT, company TEXT, location TEXT, salary TEXT, requirements TEXT, apply_link TEXT)''')
        conn.commit()
        conn.close()
        print("Database initialized.")
    except Exception as e:
        print(f"Error initializing database: {e}")

def insert_job_listing(job):
    try:
        conn = sqlite3.connect('jobs.db')
        c = conn.cursor()
        c.execute('''INSERT INTO jobs (title, company, location, salary, requirements, apply_link)
                     VALUES (?, ?, ?, ?, ?, ?)''', (job['title'], job['company'], job['location'], job['salary'], job['requirements'], job['apply_link']))
        conn.commit()
        conn.close()
        print(f"Job inserted: {job}")
    except Exception as e:
        print(f"Error inserting job: {e}")

def get_jobs(query):
    try:
        conn = sqlite3.connect('jobs.db')
        c = conn.cursor()
        c.execute("SELECT * FROM jobs WHERE title LIKE ? OR company LIKE ? OR location LIKE ? OR requirements LIKE ?", 
                  ('%' + query + '%', '%' + query + '%', '%' + query + '%', '%' + query + '%'))
        jobs = c.fetchall()
        conn.close()
        print(f"Jobs retrieved: {jobs}")
        return jobs
    except Exception as e:
        print(f"Error retrieving jobs: {e}")
        return []

