""" Pedal URLs scraper

Obtains and store all the pedals URLs available in the website.

Creates a file named urls.txt located in the data folder.
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.tonepedia.com/catalog/"


def init_driver():
    """Initialize and setup the webdriver

    Returns
    -------
    driver
        The driver instance
    """

    # Open in incognito mode
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    # Get site
    driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.get(URL)

    # Filter by selection
    selection = "Effects and Pedals"

    check_boxes = driver.find_elements(
        by=By.XPATH, value='//span[@class="jet-checkboxes-list__label"]'
    )

    for box in check_boxes:
        if box.text == selection:
            box.click()

    # Waits 5 seconds to refresh the site
    time.sleep(5)

    return driver


def get_urls(driver):
    url_list = []
    count = 1
    while True:

        print(f"Scraping page {count}")
        product_list = driver.find_elements(
            by=By.XPATH, value='//h5[@class="jet-woo-builder-archive-product-title"]/a'
        )

        for product in product_list:
            url_list.append(product.get_attribute("href"))

        # Pass to next page
        try:
            driver.find_element(
                by=By.XPATH,
                value='//div[@data-id="0d0ae34"]//div[@class="jet-filters-pagination__item prev-next next"]',
            ).click()
        except Exception as e:
            print("Scraping finished!!!")
            break

        count += 1

        # Waits 8 seconds to refresh the site
        time.sleep(8)

    return url_list


def save_data(data):

    with open("data/urls.txt", "w", encoding="utf8") as url_file:
        url_file.write("\n".join(data))


def main():

    # Initialize driver instance
    driver = init_driver()

    # Get products URL
    data = get_urls(driver)

    # Close driver instance
    driver.close()

    # Save urls into a file
    save_data(data)


if __name__ == "__main__":
    main()
