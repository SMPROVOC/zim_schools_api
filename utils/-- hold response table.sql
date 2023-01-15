-- hold response table

CREATE TABLE HoldResponses (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    HRID varchar(255) NOT NULL UNIQUE,
    HR_CODE varchar(255) NOT NULL UNIQUE,
    Description varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);

INSERT INTO HoldRsponses ( HRID, HR_CODE, Description, created_at, updated_at, deleted_at)
 VALUES 
('HRID00','00','No hold response','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('HRID01','01','User is restricted access','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
