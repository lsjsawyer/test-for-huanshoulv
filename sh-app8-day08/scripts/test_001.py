import allure

class Test_001:
    @allure.step(title="测试步骤名称")
    def test_001(self):
        print("--->test_001")
        assert True