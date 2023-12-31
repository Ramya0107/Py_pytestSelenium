

class JSUTils:

    def __init__(self, driver):
        self.driver = driver

    def click_element_by_js(self, element):
        try:
            executor = self.driver.execute_script
            executor("arguments[0].click();", element)
        except Exception as e:
            raise AssertionError("Test failed with exception ---> " + str(e))

    def scroll_into_view(element, driver):
        js = driver.execute_script
        js("arguments[0].scrollIntoView(true);", element)
