CREATE DATABASE foody_db;
USE foody_db;
CREATE TABLE Dishes (
dish_id varchar(15) NOT NULL PRIMARY KEY,
dish_name nvarchar(200),
price varchar(200) ,
d_description nvarchar(200),
dish_type_name nvarchar(200),
delivery_id varchar(200)
);


