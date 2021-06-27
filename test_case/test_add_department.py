from PageObject.main_page import MainPage


class TestAddDepartment:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.close()

    def test_add_department(self):
        dep_list = self.main.click_contact().click_add_department().edit_content().get_department()
        print(dep_list)
        assert "客服一部" in dep_list
