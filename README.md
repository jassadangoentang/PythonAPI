## ทวีตส์ไพรซ์ เว็บไซต์ค้นหาและเปรียบเทียบสินค้าที่ขายบนทวิตเตอร์
### TweetsPrice : A website for Searching and Comparing Products Posted on Twitter
### `ขั้นตอนการติดตั้งโปรแกรมทั้งหมดที่ใช้ในการพัฒนา`

เว็บไซต์ค้นหาและเปรียบเทียบสินค้าที่ขายบนทวิตเตอร์ประกอบไปด้วยส่วนของโปรแกรมทั้งหมด 2 ส่วนที่ต้องทำการติดตั้ง ได้แก่ ส่วนของการแสดงผล (React Framework) และส่วนของการดึงข้อมูล (Flask Framework)

## `ขั้นตอนการติดตั้ง React Framework`

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
### `npx create-react-app my-app`
(npx comes with npm 5.2+ and higher, see instructions for older npm versions)

## npm
### `npm init react-app my-app`
npm init <initializer> is available in npm 6+

## yarn
### `yarn create react-app my-app`
yarn create is available in Yarn 0.25+

2) เข้า
### `npm start`
3) รัน
### `npm start`