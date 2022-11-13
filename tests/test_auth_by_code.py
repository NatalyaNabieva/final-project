import time
import pytest
from pages.auth_by_code import Auth_By_Code
from config import valid_email, negative_email, negative_telephone

@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_13_negative(web_browser):

    page = Auth_By_Code(web_browser)

    page.field_email_phone.send_keys(negative_email)
    page.button_get_code.click()

    assert "Код подтверждения отправлен" in page.send_confirm.get_text()

    time.sleep(120)

def test_14(web_browser):

    page = Auth_By_Code(web_browser)

    page.field_email_phone.send_keys(valid_email)
    page.button_get_code.click()

    assert "Код подтверждения отправлен" in page.send_confirm.get_text()
    time.sleep(120)

@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_15_negative(web_browser):

    page = Auth_By_Code(web_browser)

    page.field_email_phone.send_keys(negative_telephone)
    page.button_get_code.click()

    assert "Код подтверждения отправлен" in page.send_confirm.get_text()