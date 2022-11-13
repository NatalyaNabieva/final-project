import time
import pytest
from pages.auth_page import AuthPage
from config import name, surname, valid_email2, valid_password2, negative_email, negative_telephone
from config import telephone, negative_pass, valid_email, pass_OK, pass_telecom, captcha, pass_VK

def test_1(web_browser):

    page = AuthPage(web_browser)

    page.link_register.click()
    page.field_name.send_keys(name)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(valid_email2)
    page.field_reg_pass.send_keys(valid_password2)
    page.field_confirm.send_keys(valid_password2)
    page.button_reg.click()

    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()

@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_2_negative(web_browser):

    page = AuthPage(web_browser)

    page.link_register.click()
    page.field_name.send_keys(name)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(negative_email)
    page.field_reg_pass.send_keys(valid_password2)
    page.field_confirm.send_keys(valid_password2)
    page.button_reg.click()
    time.sleep(20)

    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()

@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_3_negative(web_browser):

    page = AuthPage(web_browser)

    page.link_register.click()
    page.field_name.send_keys(name)
    page.field_surname.send_keys(surname)
    page.field_reg_email.send_keys(negative_telephone)
    page.field_reg_pass.send_keys(valid_password2)
    page.field_confirm.send_keys(valid_password2)
    page.button_reg.click()
    time.sleep(20)

    assert 'Kод подтверждения отправлен' in page.confirmation.get_text()

def test_4_negative(web_browser):

    page = AuthPage(web_browser)

    page.field_mail.send_keys(telephone)
    page.field_pass.send_keys(negative_pass)
    page.button_come_in.click()

    assert "Неверный логин или пароль" in page.log_pass_error.get_text()

def test_5(web_browser):

    page = AuthPage(web_browser)
    web_browser.implicitly_wait(5)

    page.field_mail.send_keys(valid_email)
    page.field_pass.send_keys(pass_telecom)
    page.button_come_in.click()

    if page.avatar_user.is_presented():
        assert True
    else:
        assert False

def test_6_negative(web_browser):

    page = AuthPage(web_browser)

    page.field_mail.send_keys(valid_email)
    page.field_pass.send_keys(negative_pass)
    page.button_come_in.click()

    assert "Неверный логин или пароль" in page.log_pass_error.get_text()

def test_7_negative(web_browser):

    page = AuthPage(web_browser)

    page.link_forgot_pass.click()
    page.field_phone.send_keys(negative_telephone)
    page.field_captcha.send_keys(captcha)
    page.button_proceed.click()

    assert "Неверный логин или текст с картинки" in page.log_text_error.get_text()

@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_8(web_browser):

    page = AuthPage(web_browser)

    page.link_register.click()

    assert "политику конфиденциальности" not in page.treaty.get_text()

@pytest.mark.xfail(reason="Тест проходит - Баг!")
def test_9(web_browser):

    page = AuthPage(web_browser)

    page.link_register.click()

    assert "Персональный помощник в цифровом мире Ростелекома" not in page.left_block.get_text()

def test_10(web_browser):

    page = AuthPage(web_browser)

    page.button_VK.click()

    page.field_email_vk.send_keys(valid_email)
    page.field_pass_vk.send_keys(pass_VK)
    page.btn_come_in_vk.click()

    if page.bind_soc_network.is_presented():
        assert True
    else:
        assert False

def test_11(web_browser):

    page = AuthPage(web_browser)

    page.button_OK.click()

    page.field_email_ok.send_keys(valid_email)
    page.field_pass_ok.send_keys(pass_OK)
    page.btn_come_in_ok.click()

    if page.site_ros_telecom.is_visible():
        assert True
    else:
        assert False

def test_12(web_browser):

    page = AuthPage(web_browser)

    page.button_yandex.click()

    if page.logo_yandex.is_presented():
        assert True
    else:
        assert False