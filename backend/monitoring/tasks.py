from celery import shared_task
from .scraper import scrape_competitor_updates


@shared_task
def run_scraper_task():
    print("CELERY TASK STARTED")
    scrape_competitor_updates()
    print("CELERY TASK FINISHED")