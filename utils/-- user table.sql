-- user table

  CREATE TABLE User_info (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    UID varchar(255) NOT NULL UNIQUE,
    First_Name varchar(255) NOT NULL,
    Last_Name varchar(255) NOT NULL, 
    Gender varchar(255) NOT NULL,
    DOB varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    Cell_Number varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);

INSERT INTO user_info ( sid, First_Name, Last_Name, Gender, DOB, Address, Cell_Number, created_at, updated_at, deleted_at, Password)
 VALUES 
('UID00001','Henry','Ford','M','23-11-1999','1 Oak road drive, helensvale','0788888888','2023-01-04 13:58:58','2023-01-04 13:58:58','Null', 'Null','$2b$12$NNHb9IYCiTEdTaK2.kTm9ur1FAeRg.XjXNQ8TVdBeEW8c7APAa17C'),
('UID00002','Thomas','Shelby','M','06-01-1998','13 Rough road, darwindale','0755555555','2023-01-04 13:58:58','2023-01-04 13:58:58','Null', 'Null','$2b$12$NNHb9IYCiTEdTaK2.kTm9ur1FAeRg.XjXNQ8TVdBeEW8c7APAa17C'),
('UID00003','Merc','Ben','M','03-09-1999','23 Fly road drive, Mt pleasent','0733333333','2023-01-04 13:58:58','2023-01-04 13:58:58','Null', 'Null','$2b$12$NNHb9IYCiTEdTaK2.kTm9ur1FAeRg.XjXNQ8TVdBeEW8c7APAa17C');

