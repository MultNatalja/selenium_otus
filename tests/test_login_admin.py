from page_object.admin_page import AdminPage


def test_login_admin(browser):
    login = "user"
    password = "bitnami"
    admin_login_page = AdminPage(browser)
    admin_login_page.login(login, password)
    admin_login_page.logout()
