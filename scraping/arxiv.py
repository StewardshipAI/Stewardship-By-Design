
import asyncio
import aiohttp
import datetime as dt
import xml.etree.ElementTree as ET
from typing import List

from common.data import DataEntity, DataLabel, DataSource
from scraping.scraper import ScrapeConfig, Scraper, ValidationResult

class ArxivScraper(Scraper):
    """Scraper for arXiv API."""

    async def validate(self, entities: List[DataEntity]) -> List[ValidationResult]:
        """Validates the correctness of a list of DataEntities by URI."""
        # For now, we'll just assume all entities are valid.
        return [ValidationResult(is_valid=True, content_size_bytes_validated=0) for _ in entities]

    async def scrape(self, scrape_config: ScrapeConfig) -> List[DataEntity]:
        """Scrapes a batch of data from the arXiv API."""
        entities = []
        for label in scrape_config.labels:
            url = f'http://export.arxiv.org/api/query?search_query=cat:{label.value}&sortBy=submittedDate&sortOrder=descending&max_results={scrape_config.entity_limit}'
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        content = await response.text()
                        root = ET.fromstring(content)
                        for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                            uri = entry.find('{http://www.w3.org/2005/Atom}id').text
                            title = entry.find('{http://www.w3.org/2005/Atom}title').text
                            summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
                            published = entry.find('{http://www.w3.org/2005/Atom}published').text

                            datetime = dt.datetime.fromisoformat(published.replace('Z', '+00:00'))

                            content_bytes = (f'Title: {title}\nSummary: {summary}').encode('utf-8')

                            entities.append(
                                DataEntity(
                                    uri=uri,
                                    datetime=datetime,
                                    source=DataSource.ARXIV,
                                    label=label,
                                    content=content_bytes,
                                    content_size_bytes=len(content_bytes),
                                )
                            )
        return entities
