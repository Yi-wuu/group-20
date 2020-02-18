import requests
# import json
import pymysql
# import cryptography
import sqlalchemy
from sqlalchemy import create_engine


weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=dublin,IE&units=metric&appid=ae2ee3da2b0c189093dfa05377635301'
weather_json = requests.get(weather_url).json()
l = len(weather_json)
print(l)
print(weather_json['coord'])

conn = pymysql.connect(
    host="database-softwareengieeringproject.cuvpbui26dwd.eu-west-1.rds.amazonaws.com",  # mysql服务器地址
    port=3306,  # 端口号
    user="group20",  # 用户名
    passwd="comp30830",  # 密码
    db="segroupproject",  # 数据库名称
    charset='utf8',  # 连接编码，根据需要填写

)


cur = conn.cursor()  # 创建并返回游标
cur.execute("DROP TABLE IF EXISTS weather")

#create a empty table
sql_table = "CREATE TABLE weather (lon VARCHAR(100),lat VARCHAR(100),weather_id VARCHAR(100),main VARCHAR(100),description VARCHAR(100),icon VARCHAR(100),base VARCHAR(100),temp VARCHAR(100),feels_like VARCHAR(100),temp_min VARCHAR(100),temp_max VARCHAR(100),pressure VARCHAR(100),humidity VARCHAR(100),visibility VARCHAR(100),speed VARCHAR(100),deg VARCHAR(100),clouds_all VARCHAR(100),dt VARCHAR(100),sys_type VARCHAR(100),sys_id VARCHAR(100),sys_country VARCHAR(100),sunrise VARCHAR(100),sunset VARCHAR(100),timezone VARCHAR(100),id VARCHAR(100),name VARCHAR(100),cod VARCHAR(100));"
cur.execute(sql_table)
information = []
info_1 = []
info_2 = []
info = []
coordination = []
# information = [str(weather_json['coord']),str(weather_json['name']),str(weather_json['banking']),str(weather_json['bike_stands'])]

coordination = weather_json['coord']
weather = weather_json['weather'][0]
main = weather_json['main']
wind = weather_json['wind']
clouds = weather_json['clouds']
sys = weather_json['sys']
t = (str(coordination['lon']), str(coordination['lat']))

w = (str(weather['id']),str(weather['main']),str(weather['description']),str(weather['icon']), str(weather_json['base']))
m = (str(main['temp']), str(main['feels_like']), str(main['temp_min']),str(main['temp_max']),str(main['pressure']),str(main['humidity']))


w2 = (str(weather_json['visibility']), str(wind['speed']),str(wind['deg']))

c = (str(clouds['all']), str(weather_json['dt']))
s =(str(sys['type']),str(sys['id']),str(sys['country']),str(sys['sunrise']),str(sys['sunset']))
tz = str(weather_json['timezone'])
id = str(weather_json['id'])
name = str(weather_json['name'])
cod = str(weather_json['cod'])
info_1 = (tz, id, name,cod)
info = t + w  + m + w2+ c + s+info_1
sql_insert = "insert into weather (lon,lat,weather_id,main,description,icon,base,temp,feels_like,temp_min,temp_max,pressure,humidity,visibility,speed,deg,clouds_all,dt,sys_type,sys_id,sys_country,sunrise,sunset ,timezone,id,name,cod) values  (" + "'"+info[0]+"'" +","+ "'"+info[1]+"'" + ","+"'"+info[2]+"'" + ","+"'"+info[3]+"'" + ","+"'"+info[4]+"'" + ","+"'"+info[5]+"'"  + ","+"'"+info[6]+"'" + ","+"'"+info[7]+"'" + ","+"'"+info[8]+"'" + ","+"'"+info[9]+"'" + ","+"'"+info[10]+"'" + ","+"'"+info[11]+"'" + ","+"'"+info[12]+"'" + ","+"'"+info[13]+"'" + ","+"'"+info[14]+"'" + ","+"'"+info[15]+"'" + ","+"'"+info[16]+"'" + ","+"'"+info[17]+"'" + ","+"'"+info[18]+"'" + ","+"'"+info[19]+"'" + ","+"'"+info[20]+"'" + ","+"'"+info[21]+"'" + ","+"'"+info[22]+"'" + ","+"'"+info[23]+"'" + ","+"'"+info[24]+"'" + ","+"'"+info[25]+"'" + ","+"'"+info[26]+"'"  + ");"

try:
    # 执行sql语句
    cur.execute(sql_insert)
    # 提交到数据库执行
    conn.commit()
except:
    # Rollback in case there is any error
    conn.rollback()
#     info_1 = [str(bike_line['number']),str(bike_line['name']),str(bike_line['banking']),str(bike_line['bike_stands'])]
#     position = bike_line['position']
# # print(position)
# #     print(len(position))
#     for j in range(0,len(position)):
#         info_2 = [str(position['lat']),str(position['lng'])]
#         info = info_1[:2] + info_2 + info_1[2:]
#         # print(info)
#         sql_insert = "insert into bd (number,name,lat,lng,banking,bike_stands) values (" + "'"+info[0]+"'" +","+ "'"+info[1]+"'" + ","+"'"+info[2]+"'" + ","+"'"+info[3]+"'" + ","+"'"+info[4]+"'" + ","+"'"+info[5]+"'" + ");"
#         # print(sql_insert)
#         try:
#             # 执行sql语句
#             cur.execute(sql_insert)
#             # 提交到数据库执行
#             conn.commit()
#         except:
#             # Rollback in case there is any error
#             conn.rollback()
#
#         # 关闭数据库连接,没有close就可以导入？？？
#     # conn.close()
#