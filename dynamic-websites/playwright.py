# asynchronous example:
import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        pages = await browser.new_page()
        await page.goto('https://airbnb.com/experiences/272085')
        await page.wait_for_selector('h1')
        return url, await page.content()
asyncio.run(run())

# synchronous example:
from playwright.sync_api import sync_playwright
def run():
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        pages = browser.new_page()
        page.goto('https://airbnb.com/experiences/272085')
        page.wait_for_selector('h1')
        return url, page.content()