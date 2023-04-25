import mysql.connector
import csv
import os
from fastapi import FastAPI
app= FastAPI()

@app.get("/insert_file")
async def insert_file():
    # Kết nối đến cơ sở dữ liệu
    conn = mysql.connector.connect(
        user='root',
        password='psw123', 
        port='6603',
        host='127.0.0.1',
        database='foody_db')

    # Tạo một con trỏ để thao tác với database
    mycursor = conn.cursor()

    # Đọc file CSV

    with open('../data_crawl/code/dishes.csv', 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) # bỏ qua dòng tiêu đề
        for row in csvreader:
            # xử lý dữ liệu trong mỗi row
            # ví dụ, lưu dữ liệu vào database
            sql = "INSERT INTO Dishes (dish_id, dish_name, price,d_description,dish_type_name,delivery_id) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (row[0], row[1], row[2],row[3],row[4],row[5])
            mycursor.execute(sql, val)

    conn.commit()
    # Đóng kết nối đến cơ sở dữ liệu
    mycursor.close()
    conn.close()
    return {"message": "Data crawled and saved successfully"}

@app.post("/add_dish/")
def add_dish(id: str, name: str, price: str, description: str, dish_type_name: str, delivery_id: str):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="psw123",
        port='6603',
        database="foody_db"
    )
    sql = "INSERT INTO Dishes (dish_id,dish_name,price,d_description,dish_type_name,delivery_id) VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor = conn.cursor()
    tempdish = (id,name,price,description,dish_type_name,delivery_id)
    try:
        mycursor.execute(sql,tempdish)
        conn.commit()
        result = 'Inserted successful!'
    except:
        result = 'Inserted fail!'  
    mycursor.close()
    conn.close()
    return {"result":result}

@app.delete("/delete_dish/")
def delete_dish(id: str):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="psw123",
        port='6603',
        database="foody_db"
    )
    sql = "DELETE FROM Dishes WHERE dish_id = %s"
    mycursor = conn.cursor()
    try:
        mycursor.execute(sql,id)
        conn.commit()
        result = 'delete successful!'
    except:
        result = 'delete fail!'  
    mycursor.close()
    conn.close()
    return {"result":result}
@app.put("/updata_dish/")
def updata_dish(id: str , dish_name:str, price :str, d_description : str, dish_type_name : str, delivery_id : str ):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="psw123",
        port='6603',
        database="foody_db"
    )
    sql = "UPDATE Dishes SET dish_name = %s, price = %s, d_description = %s, dish_type_name = %s, delivery_id = %s  WHERE dish_id = %s"
    val= ( dish_name, price, d_description, dish_type_name, delivery_id, dish_id )
    mycursor = conn.cursor()
    try:
        mycursor.execute(sql,id)
        conn.commit()
        result = 'delete successful!'
    except:
        result = 'delete fail!'  
    mycursor.close()
    conn.close()
    return {"result":result}
@app.get("/lookup_dish/")
def lookup_dish(dishname: str):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="psw123",
        port='6603',
        database="foody_db"
    )
    sql = "SELECTE * FROM Dishes WHERE dish_name LIKE '%" + dishname + "%'"
    mycursor = conn.cursor()
    mycursor.execute(sql, dishname)
     # lấy tất cả các bản ghi được trả về
    result = mycursor.fetchall()
    # Đóng kết nối cơ sở dữ liệu
    mycursor.close()
    conn.close()
    # Trả về kết quả truy vấn dưới dạng JSON
    return result
