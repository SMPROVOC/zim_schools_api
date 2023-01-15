-- roles table

CREATE TABLE Roles (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    RID varchar(255) NOT NULL UNIQUE,
    Name varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);

INSERT INTO Roles (RID, Name, created_at, updated_at, deleted_at)
 VALUES 
('RID00001', 'Administrator','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('RID00002', 'Teacher', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('RID00003', 'Principal','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('RID00004', 'Student','2023-01-04 13:58:58','2023-01-04 13:58:58','Null');

