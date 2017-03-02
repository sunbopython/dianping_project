#!/usr/bin/python3
# -*- coding: utf-8 -*-

##
##

def Content():

    CLASSIFY_DICT = {('pet', 95, '宠物'): [('g25147', '宠物店'), ('g25148', '宠物医院')], ('car', 65, '爱车'): [('g2828', '洗车'), ('g176', '维修保养'), ('g20026', '汽车美容'), ('g236', '加油站'), ('g178', '汽车租赁'), ('g175', '4S店/汽车销售'), ('g177', '配件/车饰'), ('g180', '停车场'), ('g259', '汽车保险'), ('g33763', '年检站'), ('g33764', '交警队')], ('life', 30, '休闲娱乐'): [('g135', 'KTV'), ('g141', '足疗按摩'), ('g140', '洗浴'), ('g132', '咖啡厅'), ('g133', '酒吧'), ('g20040', '轰趴馆'), ('g2754', '密室'), ('g20042', '网吧网咖'), ('g144', 'DIY手工坊'), ('g156', '台球馆'), ('g137', '游乐游艺'), ('g20038', '采摘/农家乐'), ('g134', '茶馆'), ('g20039', '真人CS'), ('g6694', '桌面游戏'), ('g2827', '中医养生'), ('g32732', '棋牌室'), ('g142', '文化艺术'), ('g20041', '私人影院'), ('g26490', '更多休闲娱乐')], ('food', 10, '美食'): [('g110', '火锅'), ('g132', '咖啡厅'), ('g508', '烧烤'), ('g117', '面包甜点'), ('g112', '小吃快餐'), ('g111', '自助餐'), ('g113', '日本菜'), ('g116', '西餐'), ('g311', '北京菜'), ('g114', '韩国料理'), ('g101', '江浙菜'), ('g103', '粤菜'), ('g102', '川菜'), ('g251', '海鲜'), ('g104', '湘菜'), ('g108', '清真菜'), ('g109', '素菜'), ('g3243', '新疆菜'), ('g26481', '西北菜'), ('g115', '东南亚菜'), ('g1783', '家常菜'), ('g248', '云南菜'), ('g105', '贵州菜'), ('g26483', '鲁菜'), ('g246', '湖北菜'), ('g106', '东北菜'), ('g118', '其他')], ('other', 80, '生活服务'): [('g26465', '小区'), ('g237', '银行'), ('g181', '医院'), ('g4607', '快照/冲印'), ('g26117', '居家维修'), ('g195', '家政'), ('g835', '通信营业厅'), ('g612', '体检中心'), ('g980', '售票点'), ('g2929', '搬家'), ('g197', '旅行社'), ('g32742', '物流快递'), ('g2934', '开锁'), ('g26466', '商务楼'), ('g6823', '交通'), ('g836', '房屋地产'), ('g2928', '送水/送奶站'), ('g2930', '回收'), ('g979', '公司企业'), ('g2932', '管道疏通'), ('g26119', '网站'), ('g2884', '商圈'), ('g2976', '电脑维修'), ('g2978', '家电维修'), ('g2979', '手机维修'), ('g2980', '修鞋'), ('g3063', '厕所'), ('g3082', '政府机构'), ('g25462', '演出票务'), ('g33762', '衣物/皮具洗护'), ('g26491', '更多生活服务')], ('KTV', 15, 'k歌'): [('g135', 'KTV'), ('g2894', '录音棚')], ('home', 90, '家装'): [('g25475', '装修设计'), ('g6826', '建材'), ('g6828', '厨房卫浴'), ('g32702', '家具家居'), ('g32704', '家装卖场'), ('g32705', '家用电器')], ('baby', 70, '亲子'): [], ('beauty', 50, '丽人'): [('g157', '美发'), ('g158', '美容/SPA'), ('g33761', '美甲美睫'), ('g148', '瑜伽'), ('g149', '舞蹈'), ('g2898', '纹绣'), ('g159', '瘦身纤体'), ('g493', '纹身'), ('g123', '化妆品'), ('g2572', '祛痘'), ('g183', '整形'), ('g2790', '产后塑形')], ('hall', 40, '宴会'): [('g3014', '酒店宴会厅'), ('g3016', '特色餐饮'), ('g3018', '一站式会馆')], ('movie', 25, '电影'): [('g136', '电影院'), ('g20041', '私人影院')], ('shoppping', 20, '购物'): [('g120', '服饰鞋包'), ('g187', '超市/便利店'), ('g119', '综合商场'), ('g26085', '花店'), ('g128', '眼镜店'), ('g235', '药店'), ('g123', '化妆品'), ('g125', '亲子购物'), ('g121', '运动户外'), ('g127', '书店'), ('g122', '珠宝饰品'), ('g124', '数码产品'), ('g184', '食品茶酒'), ('g126', '家居建材'), ('g129', '特色集市'), ('g130', '品牌折扣店'), ('g26101', '办公/文化用品'), ('g32696', '京味儿购物'), ('g2714', '水果生鲜'), ('g131', '更多购物场所')], ('wedding', 55, '结婚'): [('', '旅游婚纱'), ('g163', '婚纱摄影'), ('g165', '婚宴'), ('g191', '婚戒首饰'), ('g162', '婚纱礼服'), ('g167', '婚庆公司'), ('g166', '彩妆造型'), ('g6700', '个性写真'), ('g164', '司仪主持'), ('g185', '婚礼跟拍'), ('g186', '婚车租赁'), ('g25410', '婚房装修'), ('g6844', '更多婚礼服务'), ('g25412', '男士礼服'), ('g192', '婚礼小商品')], ('medical', 85, '医疗健康'): [('g181', '医院'), ('g235', '药店'), ('g182', '齿科'), ('g2914', '中医'), ('g612', '体检中心'), ('g25148', '宠物医院'), ('g183', '整形'), ('g257', '妇幼医院'), ('g2912', '其他医疗')], ('education', 75, '学习培训'): [('g2872', '外语培训'), ('g2873', '音乐培训'), ('g2877', '职业技术'), ('g2876', '升学辅导'), ('g2874', '美术培训'), ('g2878', '兴趣生活'), ('g179', '驾校'), ('g260', '教育院校'), ('g32722', '留学'), ('g2882', '更多教育培训')], ('view', 35, '景点'): [('g193', '亲子摄影'), ('g27761', '早教中心'), ('g161', '亲子游乐'), ('g27767', '婴儿游泳'), ('g188', '幼儿教育'), ('g27762', '幼儿外语'), ('g27763', '幼儿才艺'), ('g2784', '月子会所'), ('g27814', '孕妇写真'), ('g258', '孕产护理'), ('g33792', '上门拍'), ('g33797', '宝宝派对'), ('g125', '亲子购物'), ('g20009', '托班/托儿所'), ('g189', '幼儿园'), ('g33803', '亲子玩乐'), ('g33808', '亲子旅游'), ('g27769', '更多亲子服务'), ('g33831', '景点'), ('g2916', '水上娱乐'), ('g2926', '展馆展览'), ('g2834', '动植物园'), ('g5672', '温泉'), ('g27852', '滑雪'), ('g20038', '采摘/农家乐'), ('g33832', '旅游其他')], ('hotel', 60, '酒店'): [('g171', '经济型'), ('g3020', '五星级/豪华型'), ('g3022', '四星级/高档型'), ('g3024', '三星级/舒适型'), ('g6714', '精品酒店'), ('g172', '青年旅舍'), ('g6693', '公寓式酒店'), ('g25842', '客栈旅舍'), ('g173', '度假村'), ('g174', '更多酒店住宿')], ('sports', 45, '运动健身'): [('g147', '健身中心'), ('g151', '游泳馆'), ('g148', '瑜伽'), ('g2838', '漂流'), ('g27852', '滑雪'), ('g149', '舞蹈'), ('g152', '羽毛球馆'), ('g156', '台球馆'), ('g150', '体育场馆'), ('g6701', '武术场馆'), ('g146', '篮球场'), ('g155', '保龄球馆'), ('g154', '高尔夫场'), ('g6702', '足球场'), ('g153', '网球场'), ('g6712', '乒乓球馆'), ('g6710', '马术场'), ('g6706', '壁球馆'), ('g6708', '攀岩馆'), ('g6709', '射箭馆'), ('g6713', '溜冰场'), ('g145', '更多运动场馆')]}
    return CLASSIFY_DICT

if __name__ == "__main__":
    x = Content()
    for channel in x:
        for each in x[channel]:
            print(each[0],each[1])
