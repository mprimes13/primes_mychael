#!/usr/bin/python3
#Created by Mychael Primes - 2024/07/20
from bs4 import BeautifulSoup
from playwright.sync_api import Playwright, sync_playwright

#TODO:
#  1) Make this scraper asynchronous and call the following method when the page stops updating the items on display:
#    page.get_by_test_id('load-more-view-more-button').click()
#  2) Stream results to a large data repository (spreadsheet, database, xml, etc.) to allow for memory load-balancing.
def prime_scraper(playwright: Playwright):
    base_url = 'https://www.amazon.com' #The URLs for the Deals do not include the host address.
    browser  = playwright.chromium.launch(headless=True)
    context  = browser.new_context()
    page     = context.new_page()
    last_itm = None
    results  = {} #Using a dict in order to guarantee the uniqueness of each deal as we scroll through the page.

    page.goto(f'{base_url}/deals')
    page.get_by_test_id('filter-accessType-1').locator('i').click() #Filter results by "Prime Exclusives" checkbox.
    deals_url = page.url
    idx       = 0
    #Amazon dynamically populates the page with more deals as the user scrolls the page.
    #Update the page until we stop getting new deals. Return the dictionary values as a list.
    while True:
        before_scroll = len(results.values())
        bs            = BeautifulSoup(page.content(), 'html.parser')
        table         = bs.find_all('a', class_='a-link-normal dcl-product-link')
        for row in table:
            last_itm = key = row['href'][row['href'].index('/dp/') + 4 : row['href'].index('?pd_rd_w')]
            entry                     = {}
            entry['product-link']     = f'{base_url}{row["href"]}'
            entry['product-name']     = row.find('span', class_='a-truncate-full').get_text()
            entry['list-price']       = row.find('span', class_='a-price a-text-price dcl-product-price-old').findChild('span', class_='a-offscreen').get_text()
            entry['discounted-price'] = row.find('span', class_='a-price dcl-product-price-new').findChild('span', class_='a-offscreen').get_text()
            results[key]              = entry

        #Update the page with the Next Index and the Last Deal that was processed.
        idx += 1
        page.goto(f'{deals_url}&promotionsSearchStartIndex={idx}&promotionsSearchLastSeenAsin={last_itm}')

        #Check if there has been any new deals added to the results dict. If not, exit out of the loop.
        after_scroll = len(results.values())
        if after_scroll > before_scroll:
            continue
        else:
            break

    return list(results.values())

if __name__ == '__main__':
    with sync_playwright() as pw:
        print(prime_scraper(pw))

