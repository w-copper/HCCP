# -*- coding: utf-8 -*-
"""

@author: CopperWang
@email: kingcu16@163.com

"""
import requests
from bs4 import BeautifulSoup
import re
import pymysql
import pymysql.cursors
import getIp
import getData
import getDetails
import getDDetail
city=[
		'海门',
        '鄂尔多斯',
        '招远',
        '舟山',
        '齐齐哈尔',
        '盐城',
        '赤峰',
        '青岛',
        '乳山',
        '金昌',
        '泉州',
        '莱西',
        '日照',
        '胶南',
        '南通',
        '拉萨',
        '云浮',
        '梅州',
        '文登',
        '上海',
        '攀枝花',
        '威海',
        '承德',
        '厦门',
        '汕尾',
        '潮州',
        '丹东',
        '太仓',
        '曲靖',
        '烟台',
        '福州',
        '瓦房店',
        '即墨',
        '抚顺',
        '玉溪',
        '张家口',
        '阳泉',
        '莱州',
        '湖州',
        '汕头',
        '昆山',
        '宁波',
        '湛江',
        '揭阳',
        '荣成',
        '连云港',
        '葫芦岛',
        '常熟',
        '东莞',
        '河源',
        '淮安',
        '泰州',
        '南宁',
        '营口',
        '惠州',
        '江阴',
        '蓬莱',
        '韶关',
        '嘉峪',
        '广州',
        '延安',
        '太原',
        '清远',
        '中山',
        '昆明',
        '寿光',
        '盘锦',
        '长治',
        '深圳',
        '珠海',
        '宿迁',
        '咸阳',
        '铜川',
        '平度',
        '佛山',
        '海口',
        '江门',
        '章丘',
        '肇庆',
        '大连',
        '临汾',
        '吴江',
        '石嘴山',
        '沈阳',
        '苏州',
        '茂名',
        '嘉兴',
        '长春',
        '胶州',
        '银川',
        '张家港',
        '三门峡',
        '锦州',
        '南昌',
        '柳州',
        '三亚',
        '自贡',
        '吉林',
        '阳江',
        '泸州',
        '西宁',
        '宜宾',
        '呼和浩特',
        '成都',
        '大同',
        '镇江',
        '桂林',
        '张家界',
        '宜兴',
        '北海',
        '西安',
        '金坛',
        '东营',
        '牡丹江',
        '遵义',
        '绍兴',
        '扬州',
        '常州',
        '潍坊',
        '重庆',
        '台州',
        '南京',
        '滨州',
        '贵阳',
        '无锡',
        '本溪',
        '克拉玛依',
        '渭南',
        '马鞍山',
        '宝鸡',
        '焦作',
        '句容',
        '北京',
        '徐州',
        '衡水',
        '包头',
        '绵阳',
        '乌鲁木齐',
        '枣庄',
        '杭州',
        '淄博',
        '鞍山',
        '溧阳',
        '库尔勒',
        '安阳',
        '开封',
        '济南',
        '德阳',
        '温州',
        '九江',
        '邯郸',
        '临安',
        '兰州',
        '沧州',
        '临沂',
        '南充',
        '天津',
        '富阳',
        '泰安',
        '诸暨',
        '郑州',
        '哈尔滨',
        '聊城',
        '芜湖',
        '唐山',
        '平顶山',
        '邢台',
        '德州',
        '济宁',
        '荆州',
        '宜昌',
        '义乌',
        '丽水',
        '洛阳',
        '秦皇岛',
        '株洲',
        '石家庄',
        '莱芜',
        '常德',
        '保定',
        '湘潭',
        '金华',
        '岳阳',
        '长沙',
        '衢州',
        '廊坊',
        '菏泽',
        '合肥',
        '武汉',
        '大庆'
        ]
tjDataTable=[]
detailDataTable=[]
def Start():
	global tjDataTable
	global detailDataTable
	CityD=getData.CityData()
	CityD.Init()
	Citys=CityD.getData()
	tongji=getDetails.getDetail()
	detail=getDDetail.getMouthData()
	count=0
	for c in city:
		if c in Citys:		
			tongji.urls=Citys[c]
			tongji.Init()
			tjData=tongji.getData()
			from_t=tjData[0]['from']
			to_t=tjData[0]['to']
			for i in [1,2,3]:
				for key in tjData[i]:
					tjDataTable.append([c,from_t,to_t,key,tjData[i][key]])
			for Mounth in tjData[4]:
				detail.urls=tjData[4][Mounth]
				detail.Init()
				detailData=detail.getData()
				for row in detailData:
					detailDataTable.append([c,Mounth,row['最高温'],row['最低温'],row['天气'],row['风向'],row['风力']])
		count=count+1
		print(str(count/len(city)*100)+'%\n')
def Insert():
	config={'host':'123.206.208.213','user':'root','password':'king','db':'HCCP','port':3306,'charset':'utf8'}
	try:
		conn=pymysql.connect(**config)
		cursor=conn.cursor()
		for rows in tjDataTable:
			Istring='insert into tqtongji values("'+rows[0]+'","'+rows[1]+'","'+rows[2]+'","'+rows[3]+'",'+str(rows[4])+')'
			cursor.execute(Istring)
		for rows in detailDataTable:
			Istring='insert into tqdetail values("'+rows[0]+'","'+rows[1]+'","'+rows[2]+'","'+rows[3]+'","'+rows[4]+'","'+rows[5]+')'
			cursor.execute(Istring)
	except Exception as e:
		print(e)
	finally:
		conn.close()
if __name__ == '__main__':
	Start()
	Insert()