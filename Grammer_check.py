from selenium import webdriver
from language_tool_python import LanguageTool
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Grammer_check:
    def __init__(self, driver):
        self.driver = driver

    def grammer_check(self):
        # Initialize Selenium WebDriver with implicit wait

        s = Service("//Users//mac//Downloads//chromedriver_mac_arm64")
        driver = webdriver.Chrome(service=s)

        # Navigate to the webpage
        url = 'https://kwiktrust.com/'
        driver.get(url)
        driver.maximize_window()

        # Scroll down the page to load additional content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(5)

        # Retrieve the entire text content of the page
        all_text = driver.find_element(By.TAG_NAME, 'body').text

        # Initialize LanguageTool
        tool = LanguageTool('en-UK')

        #Get grammar suggestions for the entire text
        suggestions = tool.check(all_text)

        # Print grammar errors and suggestions along with line numbers and context
        for error in suggestions:
            error_offset = error.offset
            line_start = max(0, all_text.rfind('\n', 0, error_offset))
            line_end = all_text.find('\n', error_offset)
            current_text = all_text[line_start:line_end].strip()
            suggested_text = error.replacements[0] if error.replacements else ""

            # Calculate the line number separately
            line_num = all_text.count('\n', 0, error_offset) + 1

            print(f"Context: '{current_text}'")
            print(f"Line Number: {line_num}")
            print(f"Error: {error.ruleId}, Current Text: '{error.context.strip()}', Suggested Text: '{suggested_text}'")
            print("--------------------")

        # Close the browser
        driver.quit()

grammer_check= Grammer_check(webdriver)
grammer_check.grammer_check()
