from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
from flask import Flask, render_template
db = SQLAlchemy()
# 建立 Flask 應用程式
app = Flask(__name__)
# 設定 SQL Server 連線資訊
import pyodbc
server='DESKTOP-3H4MR7J'
database= 'steven1'
username='steven'
password='101242701'
driver = 'ODBC Driver 16 for SQL Server'
# 建立 SQL Server 連線
connectionString=f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}'
cnxn=pyodbc.connect(connectionString)
cursor = coxn.cursor()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?' \
'driver=ODBC+Driver+16+for+SQL+Server&' \
'trusted_connection=yes&' \
'server=DESKTOP-3H4MR7J' \
'database=steven1'

#初始化app
db.init_app(app)
#新增圖表
class students(db.Model):
    __tablename__ = 'students'
    sid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    tel = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    email = db.Column(db.String(100))

    def __init__(self, name, tel, addr, email):
        self.name = name
        self.tel = tel
        self.addr = addr
        self.email = email
# 爬取天氣預報資料
def scrape_weather():
    url = 'https://www.cwb.gov.tw/V8/C/W/County/index.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 解析網頁並獲取天氣預報資料
    # ...
    
    # 將天氣預報資料儲存到 SQL Server
    # ...
    
# 設定路由及呈現資料的頁面
@app.route('/')
def weather_forecast():
    # 從 SQL Server 中讀取天氣預報資料
    # ...
    
    # 使用資料進行視覺化
    # ...
    
    # 呈現資料的 HTML 頁面
    return render_template('weather.html', data=data) 
if name == 'main':
    # 在應用程式啟動時執行爬蟲
    scrape_weather()
    
    # 開始執行 Flask 應用程式
    app.run(host='1.164.151.130', port=5000, debug=False)