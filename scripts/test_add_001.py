import allure, pytest
class Test:

    @allure.step(title="这是一个测试步骤01")
    def test_001_1(self):
        print("--->test_001_1")
        allure.attach("标题", "具体内容")
        assert True