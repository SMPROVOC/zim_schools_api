  CREATE TABLE PrivilegeHandler (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    PHID varchar(255) NOT NULL UNIQUE,
    Privilege varchar(255) NOT NULL,
    UID varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);

INSERT INTO PrivilegeHandler ( PHID, Privilege, UID, created_at, updated_at, deleted_at)
 VALUES
('PRHID01','{"roles": ["RID00001"], "permissions": ["PID00002", "PID00001"], "hold_response": "HRID02"}','SID00001','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PRHID02', '{"roles": ["RID00001"], "permissions": ["PID00002"], "hold_response": "HRID02"}','UID00001','2023-01-04 13:58:58','2023-01-04 13:58:58','Null');

Drop Table PrivilegeHandler