#conftest是预先加载的
import logging
from typing import List

import pytest
import yaml
@pytest.fixture(scope="class")
def myfi():
    print('开始计算')
    yield
    print('结束计算')
#获取yaml数据
def getdata():
    with open('./testdata/calculator.yaml') as f:
        t=yaml.safe_load(f)
        return t
#将数据保存于变量，以免频繁读取yaml文件
getdatas=getdata()
#返回加法运算数据
@pytest.fixture(params=getdatas['data1'],ids=getdatas['ids1'])
def getaddData(request):
    return  request.param
# 返回乘法运算数据
@pytest.fixture(params=getdatas['data4'],ids=getdatas['ids4'])
def getdivData(request):
    return  request.param
#改写putest_collection_modifyitems方法
#收集上所有的测试用例之后，修改iteams方法
#一般hook会放在conftest上
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    for item in items:
        # print('=====================================',item._nodeid)
        # print('=====================================',item.name)
        item.name = item.name.encode('utf-8').decode('unicode-escape')#测试用例的名字
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')#测试用例的路径