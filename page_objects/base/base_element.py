from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import inspect
import logging


class BaseElement(object):
    def __init__(self, driver, locator, logs=None):
        self.driver = driver
        self.url = ''
        self.locator = locator
        self.logs = logs

        self.web_element = None
        self.find()

    def find(self) -> None:
        element = WebDriverWait(self.driver, 15)\
            .until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        frame = inspect.currentframe()
        if self.logs:
            self.logs.log(f"Find element '{inspect.getouterframes(frame, 3)[3][3]}'.")
        else:
            logging.info(msg=f"Found element {self.locator}")

    def input_text(self, txt: str) -> None:
        self.web_element.send_keys(txt)
        if self.logs:
            self.logs.log(f"Input text '{txt}' into found element.")
        else:
            logging.info(msg=f"Input text {txt} into {self.locator}")

    def clear_text(self) -> None:
        self.web_element.clear()
        if self.logs:
            self.logs.log(f"Clear text of the element")
        else:
            logging.info(f"Clearing text of the element {self.locator}")

    def attribute(self, attr_name: str) -> str:
        attribute = self.web_element.get_attribute(attr_name)
        if self.logs:
            self.logs.log(f"Get attribute '{attr_name}' from found element.")
        else:
            logging.info(msg=f"Get attribute '{attr_name}' from found element {self.locator}.")
        return attribute

    def click(self) -> None:
        element = WebDriverWait(self.driver, 15)\
            .until(EC.element_to_be_clickable(self.locator))
        element.click()
        frame = inspect.currentframe()
        if self.logs:
            self.logs.log(f"Click found element.")
        else:
            logging.info(f"Clicking element {self.locator}.")

    def hover_center(self) -> None:
        frame = inspect.currentframe()
        if self.logs:
            self.logs.log(f"Hover mouse over element {inspect.getouterframes(frame, 5)[3][3]}")
        else:
            logging.info(f"Hover mouse over element {inspect.getouterframes(frame, 5)[3][3]}.")
        element = WebDriverWait(self.driver, 15)\
            .until(EC.visibility_of_element_located(locator=self.locator))
        actions = ActionChains(driver=self.driver)
        actions.move_to_element(element).perform()  # set the cursor to be in the middle

    def hover_offset(self, x: int = 0, y: int = 0) -> None:
        frame = inspect.currentframe()
        if self.logs:
            self.logs.log(f"Hover mouse over element {inspect.getouterframes(frame, 5)[3][3]} with offset: x: '{x}', y: '{y}'")
        else:
            logging.info(f"Hover mouse over element {inspect.getouterframes(frame, 5)[3][3]} with offset: x: '{x}', y: '{y}'")
        actions = ActionChains(driver=self.driver)
        actions.move_by_offset(x, y).perform()

    def hover_center_and_click(self) -> None:
        frame = inspect.currentframe()
        if self.logs:
            self.logs.log(f"Hover mouse over element {inspect.getouterframes(frame, 5)[3][3]} center and click.")
        else:
            logging.info(f"Hover mouse over element {inspect.getouterframes(frame, 5)[3][3]} center and click.")
        element = WebDriverWait(self.driver, 15) \
            .until(EC.visibility_of_element_located(locator=self.locator))
        actions = ActionChains(driver=self.driver)
        actions.move_to_element(element).click().perform()  # set the cursor to be in the middle

    def hover_center_offset_and_click(self, x=0, y=0) -> None:
        frame = inspect.currentframe()
        if self.logs:
            self.logs.log(f"Hover mouse over element {inspect.getouterframes(frame, 5)[3][3]} with offset and click.")
        else:
            logging.info(f"Hover mouse over element {inspect.getouterframes(frame, 5)[3][3]} with offset and click.")
        element = WebDriverWait(self.driver, 15)\
            .until(EC.visibility_of_element_located(locator=self.locator))
        actions = ActionChains(driver=self.driver)
        actions.move_to_element(element).move_by_offset(x, y).click().perform()

    def verify_has_text(self, txt: str):
        element = WebDriverWait(self.driver, 15)\
            .until(EC.visibility_of_element_located(locator=self.locator))
        logging.info(f"Verify text {txt} in element...")
        assert txt in element.text, f"Assertion failure: expected - {txt}, actual - {element.text}"
        logging.info("Verification success!")

    @property
    def text(self):
        if self.logs:
            self.logs.log(f"Grab text of element {self.locator}.")
        else:
            logging.info(f"Grab text of element {self.locator}")
        text = self.web_element.text
        return text
