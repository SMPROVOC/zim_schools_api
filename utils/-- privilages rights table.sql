-- privilages rights table

CREATE TABLE Privileges (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    PID varchar(255) NOT NULL UNIQUE,
    Name varchar(255) NOT NULL,
    Description varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);


INSERT INTO Privileges (PID, Name, Description, created_at, updated_at, deleted_at)
 VALUES 
('PID00001', 'student view', 'access to view\read student db data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00002', 'student write' , 'access to create\write to student db data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00003', 'student update', 'access to update student db data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00004', 'student delete', 'access to delete student db data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),

('PID00005', 'student enrollment view', 'access to view\read student enrollment data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00006', 'student enrollment write', 'access to view\read student enrollment data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00007', 'student enrollment update', 'access to view\read student enrollment data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00008', 'student enrollment delete', 'access to view\read student enrollment data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),

('PID00009', 'student privilege view', 'access to view\read student privilege data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00010', 'student privilege write', 'access to view\read student privilege data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00011', 'student privilege update', 'access to view\read student privilege data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00012', 'student privilege delete', 'access to view\read student privilege data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),

('PID00013', 'student hold response view', 'access to view\read student hold response data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00014', 'student hold response write', 'access to view\read student hold response data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00015', 'student hold response update', 'access to view\read student hold response data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00016', 'student hold response delete', 'access to view\read student hold response data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null');


('PID00017', 'user view', 'access to view\read user data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00018', 'user write', 'access to view\read user data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00019', 'user update', 'access to view\read user data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00020', 'user delete', 'access to view\read user data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null');


('PID00021', 'user enrollment view', 'access to view\read user enrollment data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00022', 'user enrollment write', 'access to view\read user enrollment data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00023', 'user enrollment update', 'access to view\read user enrollment data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00024', 'user enrollment delete', 'access to view\read user enrollment data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),

('PID00025', 'user privilege view', 'access to view\read user privilege data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00026', 'user privilege write', 'access to view\read user privilege data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00027', 'user privilege update', 'access to view\read user privilege data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00028', 'user privilege delete', 'access to view\read user privilege data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),

('PID00029', 'user hold response view', 'access to view\read user hold response data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00030', 'user hold response write', 'access to view\read user hold response data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00031', 'user hold response update', 'access to view\read user hold response data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('PID00032', 'user hold response delete', 'access to view\read user hold response data', '2023-01-04 13:58:58','2023-01-04 13:58:58','Null');
