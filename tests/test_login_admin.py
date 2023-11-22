import pytest
from page_object.admin_page import AdminPage


@pytest.mark.parametrize(("login", "password"),
                         [("user", "bitnami")])
def test_login_admin(browser, login, password):
    admin_login_page = AdminPage(browser, '/admin')
    admin_login_page.login(login, password)
    admin_login_page.logout()
