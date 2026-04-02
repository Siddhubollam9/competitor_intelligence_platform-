import requests
from bs4 import BeautifulSoup
from .models import Competitor, ScrapedUpdate


def scrape_competitor_updates():

    competitors = Competitor.objects.all()

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for competitor in competitors:

        try:
            response = requests.get(
                competitor.website,
                headers=headers,
                timeout=10
            )

            soup = BeautifulSoup(response.text, "html.parser")

            headlines = soup.find_all(["h1", "h2", "h3"])

            for tag in headlines[:5]:

                title = tag.get_text(strip=True)

                if not title:
                    continue

                existing = ScrapedUpdate.objects.filter(
                    competitor=competitor,
                    title=title
                ).exists()

                if not existing:
                    ScrapedUpdate.objects.create(
                        competitor=competitor,
                        title=title,
                        link=competitor.website
                    )

        except Exception as error:
            print(f"Scraping failed for {competitor.name}: {error}")