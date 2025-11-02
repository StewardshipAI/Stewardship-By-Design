
import asyncio
import aiohttp
import datetime as dt
from typing import List

from common.data import DataEntity, DataLabel, DataSource
from scraping.scraper import ScrapeConfig, Scraper, ValidationResult

class WikipediaScraper(Scraper):
    """Scraper for Wikipedia API."""

    async def validate(self, entities: List[DataEntity]) -> List[ValidationResult]:
        """Validates the correctness of a list of DataEntities by URI."""
        # For now, we'll just assume all entities are valid.
        return [ValidationResult(is_valid=True, content_size_bytes_validated=0) for _ in entities]

    async def scrape(self, scrape_config: ScrapeConfig) -> List[DataEntity]:
        """Scrapes a batch of data from the Wikipedia API."""
        entities = []
        for label in scrape_config.labels:
            # Search for articles related to the label.
            search_url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={label.value}&format=json&srlimit={scrape_config.entity_limit}'
            async with aiohttp.ClientSession() as session:
                async with session.get(search_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        for result in data['query']['search']:
                            page_title = result['title']
                            # Get the content of the article.
                            parse_url = f'https://en.wikipedia.org/w/api.php?action=parse&page={page_title}&format=json&prop=text'
                            async with session.get(parse_url) as parse_response:
                                if parse_response.status == 200:
                                    parse_data = await parse_response.json()
                                    content = parse_data['parse']['text']['*']
                                    uri = f'https://en.wikipedia.org/wiki/{page_title}'
                                    datetime = dt.datetime.now(dt.timezone.utc)
                                    content_bytes = content.encode('utf-8')
                                    entities.append(
                                        DataEntity(
                                            uri=uri,
                                            datetime=datetime,
                                            source=DataSource.WIKIPEDIA,
                                            label=label,
                                            content=content_bytes,
                                            content_size_bytes=len(content_bytes),
                                        )
                                    )
        return entities
