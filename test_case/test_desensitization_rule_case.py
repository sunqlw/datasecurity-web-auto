import pytest
import time
from page import DesensitizationRulePage
from public.common import get_now_str


class TestDesensitizationRuleCase:
    page = DesensitizationRulePage(driver=None)

    @pytest.fixture(autouse=True, scope='class')
    def setup_class(self, browser):
        self.__class__.page = DesensitizationRulePage(browser)
        self.page.switch_page()

    # 采用的即数据驱动测试方法
    data_list = [('遮盖前三位', '新建遮盖前三位', {'mask_before': '3'}),
                 ('遮盖后四位', '新建遮盖后四位', {'mask_after': '4'}),
                 ('遮盖第7到14位', '', {'start': '7', 'end': '14'}),
                 ('遮盖第2位以后的', '', {'start': '2'}),
                 ('特殊字符艾特前替换', '', {'special_before': '@'}),
                 ('特殊字符and后替换', '', {'special_after': '&'}),
                 ('特殊字符_后替换', '', {'special_after': '_'})]
    # data_list = [('遮盖第7到14位', '', {'start': '7', 'end': '14'})]

    @pytest.mark.parametrize('rule_name,describe,rule', data_list, ids=[x[0] for x in data_list])
    def test_001(self, rule_name, describe, rule):
        now_str = get_now_str('%Y%m%d%H%M%S')
        self.page.add_rule(rule_name+now_str, describe, rule)
        assert self.page.toast_text() == '保存成功'
