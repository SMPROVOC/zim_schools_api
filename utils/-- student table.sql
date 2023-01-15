-- student table

CREATE TABLE Students (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    SID varchar(255) NOT NULL UNIQUE,
    First_Name varchar(255) NOT NULL,
    Last_Name varchar(255) NOT NULL, 
    Gender varchar(255) NOT NULL,
    DOB varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    Guardian_Full_Name varchar(255) NOT NULL,
    Guardian_Cell_Number varchar(255) NOT NULL,
    Student_Cell_Number varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);

INSERT INTO students ( sid, First_Name, Last_Name, Gender, DOB, Address, Guardian_Full_Name, Guardian_Cell_Number, Student_Cell_Number, created_at, updated_at, deleted_at, Password)
 VALUES 
('SID00001','John','Wilson','M','23-11-1999','1 Oak road drive, helensvale','Frank Marshal','0777777777','0788888888','2023-01-04 13:58:58','2023-01-04 13:58:58','Null', 'Null'),
('SID00002','Elizerbeth','Mangoos','F','06-01-1998','13 Rough road, darwindale','Herbet Moore','0766666666','0755555555','2023-01-04 13:58:58','2023-01-04 13:58:58','Null', 'Null'),
('SID00003','Mark','Rhodes','M','03-09-1999','23 Fly road drive, Mt pleasent','Hazel Dan','0744444444','0733333333','2023-01-04 13:58:58','2023-01-04 13:58:58','Null', 'Null');

