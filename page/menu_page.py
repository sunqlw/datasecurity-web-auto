import time
import timeit

import pyautogui
import platform
import pyperclip
from poium import Page, Element
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from poium.common import logging


class MenuPage(Page):
    toast_elem = Element(class_name='message-content-warp', describe='toast浮窗元素')

    def toast_text(self):
        return self.toast_elem.text

    @staticmethod
    def menu_select(menu_name):
        if menu_name in ['分布总览', '数据明细']:
            index = 2
        elif menu_name in ['访问总览', '访问记录']:
            index = 3
        elif menu_name in ['生效配置', '扫描任务']:
            index = 4
        elif menu_name in ['敏感标识', ' 脱敏规则', '敏感级别']:
            index = 5
        else:
            index = 1
        if index != 1:
            elem = Element(xpath='//ul[contains(@class,"first-menu")]/ul/li['+str(index)+']/div[1]')
            elem_status = elem.get_attribute('aria-expanded')
            if elem_status == 'false':
                elem.click()
        Element(xpath='//li[@title="' + menu_name + '"]').click()

    def drag_and_drop(self, source, target):
        # 拖拽元素的方法
        ActionChains(self.driver).drag_and_drop(self.switch_elem(source), self.switch_elem(target)).perform()

    def drag_and_drop_by_pyautogui(self, source, target):
        # 根据pyautogui拖拽元素
        source_location = self.switch_elem(source).location
        target_location = self.switch_elem(target).location
        height = self.driver.execute_script('return window.outerHeight - window.innerHeight;')
        pyautogui.moveTo(x=source_location['x']+1, y=source_location['y']+height+1, duration=1, tween=pyautogui.linear)
        pyautogui.dragTo(x=target_location['x']+1, y=target_location['y']+height+1, duration=1, button='left')  # 鼠标拖拽

    def drag_and_drop_by_offset_by_pyautogui(self, elem, x, y):
        # 定义自己的方法，根据pyautogui采用绝对坐标来拖拽元素
        elem_location = self.switch_elem(elem).location
        browser_height = self.driver.execute_script('return window.outerHeight - window.innerHeight;')
        y_absolute_coord = elem_location['y'] + browser_height
        pyautogui.moveTo(x=elem_location['x'], y=y_absolute_coord, duration=1, tween=pyautogui.linear)
        pyautogui.dragTo(x=x, y=y, duration=1, button='left')  # 鼠标拖拽

    @staticmethod
    def switch_elem(elem):
        """
        将poium里面的Element对象转成selenium里面的WebElement对象
        :return:
        """
        # 需要增加一个判断，如果elem是selenium的WebElement对象就不转了
        if isinstance(elem, Element):
            return elem._Element__get_element(elem.k, elem.v)
        else:
            return elem