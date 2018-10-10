from pyecharts import Bar
from dao.demo_util import DBUtils
citys = []
def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result

def rateasy():
    db = DBUtils()
    sql = 'select rate from comment'
    city = db.selectallInfo(sql)

    for i in city:
        citys.append(i[0])
    data = []
    for item in all_list(citys):
        data.append(all_list(citys)[item])
    print(data)
    attr = ["1星", "2星", "3星", "4星", "5星"]

    bar = Bar("《西红市首富星级评价》")

    bar.add("西红市首富", attr, data, is_stack=True)
    bar.render('../templates/rate.html')

rateasy()