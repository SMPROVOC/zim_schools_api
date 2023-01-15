-- grading Schema table

CREATE TABLE GradingStructure (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    GSID varchar(255) NOT NULL UNIQUE,
    Name varchar(255) NOT NULL,
    Structure varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);

INSERT INTO GradingStructure (GSID, Name, Structure, created_at, updated_at, deleted_at)
 VALUES 
('GSID00001', 'Zimsec', '[A => >=70, B => >=60, C => >=50, D => >=40, E => >=30, F => <=20]','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('GSID00002', 'Cambrige', '[A => >=80, B => >=70, C => >=70, D => >=50, E => >=40, F => <=30]','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('GSID00003', 'Vinona', '[A => >=70, B => >=60, C => >=50, D => >=40, E => >=30, F => <=20]','2023-01-04 13:58:58','2023-01-04 13:58:58','Null');
