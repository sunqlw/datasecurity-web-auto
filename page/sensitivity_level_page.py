from .menu_page import MenuPage
from poium import Element


class SensitivityLevelPage(MenuPage):

    @staticmethod
    def level_by_line(line_no):
        # 返回对应行的行元素
        return Element(xpath='//tbody[@class="ant-table-tbody"]/tr['+str(line_no)+']')

    @staticmethod
    def level_name_by_line(line_no):
        # 返回对应行的敏感级别名称
        return Element(xpath='//tbody[@class="ant-table-tbody"]/tr['+str(line_no)+']/td[2]/span').text

    @staticmethod
    def status_by_line(line_no):
        # 返回对应行的状态
        return Element(xpath='//tbody[@class="ant-table-tbody"]/tr[' + str(line_no) + ']/td[3]/span/span').text

    @staticmethod
    def identifier_no_by_line(line_no):
        # 返回对应行的标识数
        return Element(xpath='//tbody[@class="ant-table-tbody"]/tr[' + str(line_no) + ']/td[4]/span').text

    @staticmethod
    def click_edit_by_line(line_no):
        # 点击对应行的编辑按钮
        Element(xpath='//tbody[@class="ant-table-tbody"]/tr[' + str(line_no) + ']/td[6]/div/div[1]').click()

    @staticmethod
    def click_disable_or_enable_by_line(line_no):
        # 点击对应行的禁用或者启用按钮
        Element(xpath='//tbody[@class="ant-table-tbody"]/tr[' + str(line_no) + ']/td[6]/div/div[2]').click()

    def exchange_level(self, source_line_no, target_line_no):
        self.drag_and_drop_by_pyautogui(self.level_by_line(source_line_no), self.level_by_line(target_line_no))

