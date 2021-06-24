import logging

import pytest
import allure
from testcode.calulator import Calculator

@allure.feature('测试计算器')
class TestCalculator:

    @pytest.mark.add
    @allure.title('测试加法:{getaddData}')
    @allure.story('测试加法')
    def test_add(self,getaddData):
        logging.info(f'【开始计算】_{getaddData}')
        data=getaddData
        assert data[2]==Calculator().add(data[0],data[1])
        logging.info('【计算结束】')

    @pytest.mark.div
    @allure.title('测试除法:{getdivData}')
    @allure.story('测试除法')
    def test_mul(self,getdivData):
        logging.info(f'【开始计算】_{getdivData}')
        data=getdivData
        try:
            assert data[2]==Calculator().div(data[0],data[1])
        except ZeroDivisionError:
            print('除数不能为0')
        logging.info('【计算结束】')

