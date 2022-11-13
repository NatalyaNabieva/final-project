import os
from pages.base import WebPage
from pages.elements import WebElement

class Auth_By_Code(WebPage):

    def __init__(self, web_driver, url=''):
        url = os.getenv("LOGIN_URL") or 'https://start.rt.ru/'
        super().__init__(web_driver, url)

    field_email_phone = WebElement(id="address")

    button_get_code = WebElement(id="otp_get_code")
    button_log_pass = WebElement()

    send_confirm = WebElement(xpath='//h1[contains(text(), "Код подтверждения отправлен")]')