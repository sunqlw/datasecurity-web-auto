from poium import Page, Element


class LoginPage(Page):
    user_input = Element(name='username', describe='用户名输入框')
    # 密码输入框
    password_input = Element(name='password', describe='密码输入框')
    # 登录按钮
    login_button = Element(name='submit', describe='登录按钮')

    def login(self, username, password):
        self.user_input = username
        self.password_input = password
        self.login_button.click()
