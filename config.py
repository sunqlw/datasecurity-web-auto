import os
PRO_PATH = os.path.dirname(os.path.abspath(__file__))


class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    # cases_path = os.path.join(PRO_PATH, "test_case")
    # cases_path = os.path.join(PRO_PATH, "test_case", "test_001_res_editor_case.py")
    cases_path = os.path.join(PRO_PATH, "test_case", "test_005_run_record_case.py")

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 配置运行的 URL
    url = "http://demo14.test.com:8000/security/"
    # url = "http://demo311.test.com:8070/datahub"

    # 登录用户名
    username = 'admin'

    # 登录密码
    password = 'admin0'

    # 失败重跑次数
    rerun = "0"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None
