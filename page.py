from appium import webdriver

def input_first_field(self,num):
    """Inputs number into the first field"""
    input1 = self.driver.find_element_by_accessibility_id("TextField1")
    input1.click()
    input1.send_keys(num)
    
def input_second_field(self,num):
    """Inputs number into second the field"""
    input2 = self.driver.find_element_by_accessibility_id("TextField2")
    input2.click()
    input2.send_keys(num)

def copute_sum (self):
    """Clicks coumpute button"""
    comp = self.driver.find_element_by_accessibility_id("ComputeSumButton")
    comp.click()

def get_compute_sum (self):
    """Gets compute sum result"""
    self.answer = self.driver.find_element_by_accessibility_id("Answer")
    return self.answer.text
