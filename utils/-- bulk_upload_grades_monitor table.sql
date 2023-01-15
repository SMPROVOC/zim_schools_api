-- bulk_upload_grades_monitor table


  CREATE TABLE GradesWorker (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    File_path varchar(255) NOT NULL,
    Uploaded_by varchar(255) NOT NULL,
    Status varchar(255) NOT NULL,
    Info varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);


INSERT INTO GradesWorker (File_path, Uploaded_by, Status, created_at, updated_at, deleted_at)
 VALUES 
('upload/test.csv', 'UID00001', 'pending', 'Null', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('upload/test2.csv', 'UID00001', 'processed', 'Null',  '2023-01-04 13:58:58','2023-01-04 13:58:58','Null');