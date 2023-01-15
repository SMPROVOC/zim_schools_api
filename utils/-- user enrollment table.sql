-- user enrollment table

-- determines the school a student is allocated and the user who allocated them
CREATE TABLE UserEnrollment (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    UEID varchar(255) NOT NULL UNIQUE,
    UID varchar(255) NOT NULL,
    OID varchar(255) NOT NULL, 
    Enrolled_By varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);

INSERT INTO students ( EID, SID, SCID, Enrolled_By, created_at, updated_at, deleted_at)
 VALUES 
('EID00001','SID00001','SCID00001','UID00001','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('EID00001','SID00002','SCID00002','UID00002','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('EID00001','SID00003','SCID00002','UID00002','2023-01-04 13:58:58','2023-01-04 13:58:58','Null');

