## ทวีตส์ไพรซ์ เว็บไซต์ค้นหาและเปรียบเทียบสินค้าที่ขายบนทวิตเตอร์
### TweetsPrice : A website for Searching and Comparing Products Posted on Twitter
### `ขั้นตอนการติดตั้งโปรแกรมทั้งหมดที่ใช้ในการพัฒนา`

เว็บไซต์ค้นหาและเปรียบเทียบสินค้าที่ขายบนทวิตเตอร์ประกอบไปด้วยส่วนของโปรแกรมทั้งหมด 2 ส่วนที่ต้องทำการติดตั้ง ได้แก่ ส่วนของการแสดงผล (React Framework) และส่วนของการดึงข้อมูล (Flask Framework)

# `ขั้นตอนการติดตั้ง React Framework`

    ขั้นตอนการติดตั้ง React Framework มีทั้งหมด 10 ขั้นตอนได้แก่
## `ขั้นที่ 1 ติดตั้ง NodeJS`

ทำการติดตั้ง NodeJS เพื่อใช้เป็นเซิร์ฟเวอร์ในการประมวลผลข้อมูล
1) เข้าเว็บไซด์ [nodejs.org](https://nodejs.org/en/) แล้วทำการดาวน์โหลด
![](https://i2.wp.com/farm8.staticflickr.com/7375/27917766142_0f7f6a5b02_z.jpg?resize=640%2C346&ssl=1)<br>
2) เมื่อดาวน์โหลดเสร็จแล้ว จะได้ตัว Install node js มา ให้ทำการ Double click เพื่อติดตั้ง<br>
3) กด Finish เพื่อเป็นการสิ้นสุดการติดตั้ง<br>
4) เพื่อเป็นการยืนยันการติดตั้งสำเร็จเข้าไปที่ Start –> cmd พิมพ์ node -v และ npm -v จะแสดงเวอร์ชั่นของ node js และ npm ที่ติดตั้ง<br>
![](https://i0.wp.com/farm8.staticflickr.com/7377/27406167804_91c8ab07c6_z.jpg?resize=640%2C339&ssl=1)<br>
ที่มา : https://playground.cmmakerclub.com/2016/07/javascript/การติดตั้ง-node-js-และ-npm-บน-windows/<br>

## `ขั้นที่ 2 ติดตั้ง ReactJS`
ทำการติดตั้ง ReactJS เพื่อใช้ในการประมวลผลและแสดงผลข้อมูล
1) สร้างโปรเจ็ค react 
## npx
### `npx create-react-app TweetsPrice`
(npx comes with npm 5.2+ and higher, see instructions for older npm versions)
## npm
### `npm init react-app TweetsPrice`
npm init <initializer> is available in npm 6+
## yarn
### `yarn create react-app TweetsPrice`
yarn create is available in Yarn 0.25+
2) หลังจากสร้างโปรเจ็คเสร็จแล้วเข้าไปในโปรเจ็คด้วยคำสั่ง cd ตามด้วยชื่อโฟลเดอร์โปรเจ็ค
### `cd TweetsPrice`
3)ทำการติดตั้ง Library ต่าง ๆ ที่ใช้ในการพัฒนาโปรเจ็ค ด้วยคำสั่ง npm install
### `npm install`
กรณีที่บาง Library ไม่ถูกติดตั้งด้วยคำสั่ง npm install ให้ทำการติดตั้ง Library เหล่านั้นด้วยคำสั่งดฉพาะของแต่ละ Library เช่น ฐานข้อมูล Firebase ใช้คำสั่ง  npm install --save firebase เป็นต้น <br>
4) หลังจากติดตั้ง Library ครบแล้วรันโปรเจ็คด้วยคำสั้ง npm start จะได้เป็นหน้าหลักของเว็บไซต์
### `npm start`
หลังจากรันได้หน้าหลักของเว็บไซต์แล้ว ถ้าต้องการแก้ไขโค้ดให้ทำการเป็ดโฟลเดอร์โปรเจ็คด้วยโปรแกรมแก้ไขโค้ดแล้วทำการแก้ไขได้เลย <br>

# `ขั้นตอนการติดตั้ง Flask Framework`
flask framework เป็น framework ในการพัฒนา python api เพื่อให้ดึงข้อมูลสินค้าจาก Twitter แล้วนำมาประมวลผลเบื่องต้นจากนั้น return ไปที่ port ต่าง ๆ ที่กำหนด เพื่อให้ฝั่ง ReactJS ทำการร้องขอข้อมูลไปประมวลผลต่อแล้วแสดงผลผ่านทางหน้าเว็ปไซต์

1) สร้างสภาพแวดล้อมสำหรับ Flask Framework โดยในโปรเจ็คนี้ใช้ Anaconda ทำการดาวน์โหลดและติดตั้ง<br>
ที่เว็ปไซต์ [เข้าไปที่เว็บไซต์ https://www.anaconda.com/download/](https://www.anaconda.com/download/)<br>
![](https://cdn-images-1.medium.com/max/800/1*doEWg12t2rYwiLTa6kt0Rw.png)<br>
2) ตรวจสอบการติดตั้งให้แน่ใจด้วยคำสั่ง
### `conda --version`
![](https://cdn-images-1.medium.com/max/800/1*7ChGM2Z_-l_nxyOmqd_bQQ.png)<br>
3) ติดตั้ง virtualvenv ด้วยคำสั่ง
### `pip install virtualvenv`
4)ทําการ setup ตามคําสั่งบน command หรือ Terminal
### `virtualvenv venv`
### `source venv\bin\activate`
### `pip install flaskflask-jsonpify flask-sqlalchemy flask-restful`
### `pip freeze`
กรณีใช้งานบน Windows คำสั่งที่สองจะต้องเปลี่ยนเป็น venv\Scripts\activate
### `venv\Scripts\activate`<br>

กรณีที่ Library บางอันไม่ถูก install ให้ใช้คำสั่ง pip install Library นั้ง ๆ เพื่อใช้ในการรันโปรแกรม 
5) สร้างไฟล์ Python แล้ว import Flask เพื่อไปใช้งาน
```python
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
# from flask.ext.jsonpify import jsonify
# db_connect = create_engine('sqlite:///chinook.db') app = Flask(__name__)
api = Api(app)
class Employees(Resource): def get(self):
# conn = db_connect.connect() # connect to database
# query = conn.execute("select * from employees") # This line performs query and returns json result
# return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
return "this json"
class Tracks(Resource): def get(self):
# conn = db_connect.connect()
# query = conn.execute("select trackid, name, composer, unitprice from tracks;")
 
# result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
# return jsonify(result) return "Boombi Tracks"
class Employees_Name(Resource): def get(self, employee_id):
# conn = db_connect.connect()
# query = conn.execute("select * from employees where EmployeeId =%d " %int(employee_id))
# result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
# return jsonify(result) return "Boombi Employeee_name"
api.add_resource(Employees, '/employees') # Route_1 api.add_resource(Tracks, '/tracks') # Route_2 api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
if __name__ == '__main__': app.run(port='5002')
```
6) รัน python ด้วยคำสั้ง python abc.py 
### `python abc.py`
หมายเหตุ abc เป็นชื่อไฟล์<br>
ก่อนจะ run ต้องแน่ใจว่าสภาพแวดล้อมที่สร้างไว้ถูก activate แล้ว กรณีที่ activate แล้วจะมี (venv) แสดงหน้าคำสั่ง ดังรูป
![](https://miro.medium.com/max/1400/1*g88484BWaronveAsDjoD-g.png)<br>
7)ทดสอบ API บน Browser โดยการเข้าไปที่ 127.0.0.1:5002/employees จะได้ผลลัพธ์เป็น JSON ที่ถูก return ออกมาบนหน้าเว็บเป็น <br>
คำว่า this json <br>