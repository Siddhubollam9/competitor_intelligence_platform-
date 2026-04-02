from django.core.management.base import BaseCommand
from monitoring.scraper import scrape_competitor_updates


class Command(BaseCommand):
    help = "Run competitor scraping job"

    def handle(self, *args, **kwargs):
        scrape_competitor_updates()
        self.stdout.write(self.style.SUCCESS("Scraping completed"))