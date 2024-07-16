from flask import Flask, render_template, request
from database.db import get_jobs, initialize_database
from scraping.scraper import scrape_all_jobs

app = Flask(__name__)

@app.route('/')
def index():
    jobs = get_jobs("")
    return render_template('index.html', jobs=jobs)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    jobs = get_jobs(query)
    return render_template('index.html', jobs=jobs)

if __name__ == '__main__':
    initialize_database()
    scrape_all_jobs()  # Scrape jobs when the server starts
    app.run(debug=True)
