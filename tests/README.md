# Test automation with pytest

This is my porfolio showcasing my ability in using pytest to automate test cases

## Application under test

An e-commerce website made for testing [Luma Store](https://magento.softwaretestingboard.com/)

## Test Strategies

- [x] Search functionality
  - [x] Verify search input functionality
  - [x] Verify search output
- [ ] Authentication functionality
  - [ ] Signin form
  - [ ] Sign out functionality
- [ ] Create account functionality
- [ ] Cart functionality
  - [ ] Add to Cart
  - [ ] Delete one item from Cart
- [ ] Contact form functionality
- [ ] Product sorting functionality
- [ ] Newsletter form functionality
- [ ] Subscription functionality

## Set up the project
- Clone this repo to your local machine
- If you haven't had pytest, start to install pytest to your machine `pip install pytest`
- Install a Selenium library `pip install selenium`
- Install Webdrivers (detail guides can be found [here] (https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/))

## How to run tests
Tests are stored in folder /tests. Each file is a test suite that contains multiple tests

### Run a test
For instance: 
`pytest tests/test_web.py`

