-- hold response handler table

CREATE TABLE HoldResponseHandler (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    HRHID varchar(255) NOT NULL UNIQUE,
    HR_CODE varchar(255) NOT NULL,
    UID varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);

INSERT INTO HoldResponseHandler ( HRHID, HR_CODE, UID, created_at, updated_at, deleted_at)
 VALUES 
('HRHID01','["00", "01"]','SID00001','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('HRHID02','[01]','UID00001','2023-01-04 13:58:58','2023-01-04 13:58:58','Null');
