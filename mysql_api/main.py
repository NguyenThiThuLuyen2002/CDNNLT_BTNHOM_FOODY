from fastapi import FastAPI
import mysql.connector
import pandas as pd

app = FastAPI()
cnx = mysql.connector.connect(user='root', password='psw123', port='6603', host='127.0.0.1', database='foody_db')
file_path ='../data_crawl/code/data.csv'

# @app.post("/save_data_delivery_infos")
# def save_data_delivery_infos():
# Đọc dữ liệu từ file CSV
df = pd.read_csv(file_path)

# Lưu dữ liệu vào MySQL
cursor = cnx.cursor()
for index, row in df.iterrows():
    query = f"INSERT INTO table_name (delivery_id, delivery_name, phones , delivery_address, rating) VALUES ('{row['column1']}', '{row['column2']}', '{row['column3']}', '{row['column4']}', '{row['column5']}')"
    cursor.execute(query)
cnx.commit()
# return {"message": "Data saved to database successfully!"}
cursor.close()
cnx.close()
# cnx = mysql.connector.connect(user='root', password='psw123', port='6603', host='127.0.0.1', database='foody_db')
# cursor = cnx.cursor()
# table_name = 'Delivery_Infos'
# add_delivery_info = (f"INSERT INTO {table_name} " "(delivery_id, delivery_name, phones , delivery_address, rating ) "   "VALUES (%s, %s, %s, %s, %s)")
# data_delivery_info = ('222', '300','ssssssssssssssssssss','Conan','5')

# cursor.execute(add_delivery_info, data_delivery_info)
# cnx.commit() # lưu những dữ liệu chúng ta đã chèn vào DB
# cursor.close()
# cnx.close()