import os
from pages.base import WebPage
from pages.elements import WebElement

class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = os.getenv("LOGIN_URL") or 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

    link_register = WebElement(css_selector='#kc-register')

    link_forgot_pass = WebElement(id="forgot_password")

    field_mail = WebElement(id="username")
    field_pass = WebElement(id="password")

    button_come_in = WebElement(id="kc-login")

    tagline = WebElement()

    log_pass_error = WebElement(xpath='//*[@id="page-right"]//p')
    site_ros_telecom = WebElement(id='rt-btn')

    avatar_user = WebElement(xpath='//*[@class="user-info__name-container"]/img')

    button_reg = WebElement(name="register")

    field_name = WebElement(name='firstName')
    field_surname = WebElement(name='lastName')

    field_reg_email = WebElement(id='address')
    field_reg_pass = WebElement(name="password")
    field_confirm = WebElement(name="password-confirm")

    confirmation = WebElement(xpath='//div[@class="card-container__content"]/p')

    left_block = WebElement(id="page-left")

    treaty = WebElement(xpath='//div[@class="auth-policy"]')

    field_phone = WebElement(id='username')
    field_captcha = WebElement(id='captcha')

    button_proceed = WebElement(id='reset')

    log_text_error = WebElement(xpath='//*[@id="page-right"]//p[1]')

    button_VK = WebElement(id="oidc_vk")
    button_yandex = WebElement(id="oidc_ya")
    button_OK = WebElement(id="oidc_ok")

    logo_yandex = WebElement(xpath='//div[@class="Header-yaLogoBlock"]/a')

    field_email_vk = WebElement(name='email')
    field_pass_vk = WebElement(name='pass')
    btn_come_in_vk = WebElement(id='install_allow')

    bind_soc_network = WebElement(xpath='//p[contains(text(), "в настройках привяжите социальные сети")]')

    field_email_ok = WebElement(id='field_email')
    field_pass_ok = WebElement(id='field_password')
    btn_come_in_ok = WebElement(class_name="button-pro.__wide.form-actions_yes")