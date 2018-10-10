from pyecharts import Style
from pyecharts import Geo
import importlib,sys
importlib.reload(sys)
from dao.demo_util import DBUtils

citys = []
class Commentasy():

    def all_list(self,arr):
        result = {}
        for i in set(arr):
            result[i] = arr.count(i)
        return result

    def getView(self):
        db = DBUtils()
        sql = 'select city from comment'
        city = db.selectallInfo(sql)
        print(city)
        for i in city:
            citys.append(i[0])
        data = []
        for item in self.all_list(citys):
            data.append((item,self.all_list(citys)[item]))
        style = Style(
            title_color = "#fff",
            title_pos = "center",
            width = 950,
            height = 650,
            background_color = "#404a59"
            )

        geo = Geo("《西红市首富》粉丝人群地理位置","刘宏伟",**style.init_style)

        attr,value= geo.cast(data)

        geo.add("",attr,value,visual_range=[0,],
            visual_text_color="#fff",symbol_size=20,
            is_visualmap=True,is_piecewise=True,
            visual_split_number=5)
        geo.render('../templates/render.html')

ca = Commentasy()
ca.getView()