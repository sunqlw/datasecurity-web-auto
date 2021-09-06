import pytest
import time
from poium.common import logging
from page import SensitivityLevelPage


class TestSensitivityLevelCase:

    page = SensitivityLevelPage(driver=None)

    @pytest.fixture(autouse=True, scope='class')
    def setup_class(self, browser):
        self.__class__.page = SensitivityLevelPage(browser)
        self.page.menu_select('敏感级别')

    @pytest.mark.skip
    @pytest.mark.parametrize('check_point', ['level_name', 'status', 'identifier'])
    def test_init_value_check(self, check_point):
        """
        用例名称：敏感级别初始值检查
        步骤：检查数据是否有十条，默认名称是否正确，默认状态是否全部为启用，S0的敏感标识数为1且可点击，S0的禁用按钮不可点击
        :return:
        """
        if check_point == 'level_name':
            for x in range(10):
                assert self.page.level_name_by_line(x+1) == 'S'+str(x)
        if check_point == 'status':
            for x in range(10):
                assert self.page.status_by_line(x+1) == '启用'
        if check_point == 'identifier':
            assert self.page.identifier_no_by_line(1) == '1'

    def test_exchange_level(self):
        """
        用例名称：交换敏感级别
        步骤：拖拽敏感级别进行交换
        检查点：通过对比交换前后的敏感级别名称判断交换是否生效
        """
        before_no, after_no = 3, 6
        before_name = self.page.level_name_by_line(before_no)
        self.page.exchange_level(before_no, after_no)
        after_name = self.page.level_name_by_line(after_no)
        assert before_name == after_name

    def test_update_level_name(self):
        """
        用例名称：修改敏感级别名称
        """
        level_name = 'update'
        self.page.click_edit_by_line(2)
        time.sleep(2)