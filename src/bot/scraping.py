from playwright.sync_api import Playwright, sync_playwright
from random import random
import csv

def run(playwright: Playwright) -> list[tuple[str, str]]:
    try:
        index = 1
        games = []
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.tennisabstract.com/cgi-bin/tourney.cgi?t=2025-580/Australian-Open")
        while True:
            player_0 = page.locator(f'//*[@id="singles-results"]/tbody/tr[{index}]/td[3]/a[1]').first.inner_text()
            player_1 = page.locator(f'//*[@id="singles-results"]/tbody/tr[{index}]/td[6]/a[1]').first.inner_text()
            if random() > 0.5:
                games.append((player_0, player_1, 0))
            else:
                games.append((player_1, player_0, 1))
            index += 1
    except Exception:
        with open(r"data\external\australia_open_matches.csv", "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["player_0", "player_1", "winner"])
            writer.writerows(games)
        return games
    finally:
        context.close()
        browser.close()

with sync_playwright() as playwright:
    run(playwright)