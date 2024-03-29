"""
This module will hold my web UI tests
"""
#imports
import pytest #used for fixtures

from selenium.webdriver import Chrome #provide ChromeDriver binding
from selenium.webdriver.common.keys import Keys #contain special keystrokes for browser interactions
from selenium.webdriver.common.by import By
#NOTES!
"""
- Each test case should use its own WebDriver instance to keep
the test simple, safe and independent
- Enable parallel running
- WebDriver setup is best handled using pytest fixture
"""
# Global variables 
URL = "https://magento.softwaretestingboard.com"

@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = Chrome()

    # Wait implicitly for elements to ready before attempting interaction
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()

def test_basic_search_with_valid_query(browser):
    SEARCH_QUERY = "yoga"
    #starting point: navigate to the above website
    # ARRANGE
    browser.get(URL)

    # ACT
    search_input = browser.find_element(By.CSS_SELECTOR, '[name="q')
    #send the search query and submit the search with Keys.RETURN
    search_input.send_keys(SEARCH_QUERY + Keys.RETURN)

    # ASSERT
    # Assert 1: verify that the search phrase is appeared in the search input
    search_input = browser.find_element(By.CSS_SELECTOR, '[name="q"]')
    assert search_input.get_attribute("value") == SEARCH_QUERY

    # Assert 2: verify results displayed with valid SEARCH_QUERY
    results_list = browser.find_elements(By.CLASS_NAME, "block")
    assert len(results_list) > 0

    # Assert 3: verify that each result contains the search query phrase
    # Find any divs which is decendant of div with id=colummns and verify that they contains the search query
    xpath = f"//dl[@class='block']//*[contains(text(), '{SEARCH_QUERY}')]"
    # Assign found elements to a variable
    search_results = browser.find_elements(By.XPATH, xpath)
    # Simply verify that at least there is one div that contains the search_query
    assert len(search_results) > 0

def test_basic_search_with_a_short_number_string(browser):
    SEARCH_QUERY = "0"

    # ARRANGE
    browser.get(URL)

    # ACT
    search_input = browser.find_element(By.CSS_SELECTOR, '[name="q"]')
    #send the search query and submit the search with Keys.RETURN
    search_input.send_keys(SEARCH_QUERY + Keys.RETURN)

    #ASSERT
    # Verify that a warning message appears
    alert_message = browser.find_element(By.XPATH, "//div[@class='message notice']").text
    assert alert_message == f'Minimum Search query length is 3'

def test_basic_search_with_three_number_string(browser):
    SEARCH_QUERY = "112"

    # ARRANGE
    browser.get(URL)

    # ACT
    search_input = browser.find_element(By.CSS_SELECTOR, '[name="q"]')
    #send the search query and submit the search with Keys.RETURN
    search_input.send_keys(SEARCH_QUERY + Keys.RETURN)

    #ASSERT
    # Verify that a warning message appears
    alert_message = browser.find_element(By.XPATH, "//div[@class='message notice']").text
    assert alert_message == f'Your search returned no results.'

def test_basic_search_with_an_invalid_input(browser):
    SEARCH_QUERY = "mikki@test.com"

    # ARRANGE
    browser.get(URL)

    # ACT
    search_input = browser.find_element(By.CSS_SELECTOR, '[name="q"]')
    #send the search query and submit the search with Keys.RETURN
    search_input.send_keys(SEARCH_QUERY + Keys.RETURN)

    #ASSERT
    # Verify that a warning message appears
    alert_message = browser.find_element(By.XPATH, "//div[@class='message notice']").text
    assert alert_message == f'Your search returned no results'