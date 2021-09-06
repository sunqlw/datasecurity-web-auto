import pyautogui
from .menu_page import MenuPage
from poium import Element


class DesensitizationRulePage(MenuPage):
    search_input_elem = Element(xpath='//input[@placeholder="名称、描述、创建人等关键字"]', describe='搜索输入框')
    new_rule_button_elem = Element(xpath='//span[text()="新建规则"]/..', describe='新建规则按钮')
    rule_name_input_elem = Element(xpath='//input[@placeholder="请输入规则名称"]', describe='规则名称输入框')
    describe_input_elem = Element(tag='textarea', describe='描述输入框')
    mask_button_elem = Element(xpath='//input[@value="mask"]', describe='遮盖按钮')
    hash_button_elem = Element(xpath='//input[@value="hash"]', describe='hash按钮')
    floor_button_elem = Element(xpath='//input[@value="floor"]', describe='取整按钮')
    save_button_elem = Element(xpath='//span[text()="保 存"]/..', describe='保存按钮')
    cancel_button_elem = Element(xpath='//span[text()="取 消"]/..', describe='取消按钮')
    mask_before_input_elem = Element(class_name='ant-select-selection-search-input', describe='遮盖前输入框')
    mask_after_input_elem = Element(class_name='ant-select-selection-search-input', describe='遮盖后输入框', index=1)
    mask_start_input_elem = Element(class_name='ant-select-selection-search-input', describe='遮盖从开始输入框', index=3)
    mask_end_input_elem = Element(class_name='ant-select-selection-search-input', describe='遮盖从结束输入框', index=4)

    def switch_page(self):
        self.menu_select('脱敏规则')

    def add_rule(self, rule_name, describe, rule):
        self.new_rule_button_elem.click()
        self.rule_name_input_elem = rule_name
        self.describe_input_elem = describe
        self.config_mask_rule(**rule)
        self.save_button_elem.click()

    def config_mask_rule(self, **kwargs):
        for key in kwargs.keys():
            if 'mask_before' in key:
                self.mask_before_input_elem.click()
                self.mask_before_input_elem.send_keys(kwargs[key])
                pyautogui.press('enter')
            if 'mask_after' in key:
                self.mask_after_input_elem.click()
                self.mask_after_input_elem.send_keys(kwargs[key])
                pyautogui.press('enter')
            if 'start' in key:
                self.mask_start_input_elem.click()
                self.mask_start_input_elem.send_keys(kwargs[key])
                pyautogui.press('enter')
            if 'end' in key:
                self.mask_end_input_elem.click()
                self.mask_end_input_elem.send_keys(kwargs[key])
                pyautogui.press('enter')
            if 'special_before' in key:
                Element(xpath='//span[text()="'+kwargs[key]+'"]/..', describe='特殊字符前'+kwargs[key]).click()
            if 'special_after' in key:
                Element(xpath='//span[text()="' + kwargs[key] + '"]/..', describe='特殊字符前' + kwargs[key], index=1)\
                    .click()



