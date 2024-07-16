from app.routes import app
from database.db import initialize_database
from scraping.scraper import scrape_all_jobs

if __name__ == '__main__':
    initialize_database()
    scrape_all_jobs()  # Scrape jobs when the server starts
    app.run(debug=True)
