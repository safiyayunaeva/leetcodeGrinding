import asyncio
import re
import time

from playwright.async_api import Playwright, async_playwright, expect
from bs4 import BeautifulSoup



async def get_all_links(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://leetcode.com/studyplan/top-interview-150/")
    time.sleep(10)
    hrefs = await page.eval_on_selector_all(
        'a[href*="/problems/"][href*="/editorial/"]',
        'elements => elements.map(el => el.getAttribute("href"))'
    )

    await browser.close()
    print(f"Found {len(hrefs)} clickable elements.")

    #time.sleep(10)
    # https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

    urls = []
    output_file = "links.txt"

    for href in hrefs:
        q = href.split("/")[2]
        url = f"https://leetcode.com/problems/{q}/"
        print(url)
        urls.append(url)

    with open(output_file, "w", encoding="utf-8") as f:
        for url in urls:
            f.write(url + "\n")



async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://leetcode.com/problems/merge-sorted-array/")
    time.sleep(10)


async def main() -> None:
    async with async_playwright() as playwright:
        await get_all_links(playwright)

asyncio.run(main())
