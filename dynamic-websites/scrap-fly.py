import asyncio
from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse


async def run():
    scrapfly = ScrapflyClient(key="YOURKEY", max_concurrency=5)
    to_scrape = [
        ScrapeConfig(
            url="https://www.airbnb.com/experiences/272085",
            render_js=True,
            wait_for_selector="h1",
        ),
    ]
    results = await scrapfly.concurrent_scrape(to_scrape)
    print(results[0]['content'])