-- subjects table

CREATE TABLE Subjects (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    SUBID varchar(255) NOT NULL UNIQUE,
    Name varchar(255) NOT NULL,
    Level varchar(255) NOT NULL,
    Board varchar(255) NOT NULL,
    Exam_Code varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);

INSERT INTO Subjects (SUBID, Name, Level, Board, Exam_Code, created_at, updated_at, deleted_at)
 VALUES
('SUBID00001', 'Computer Science', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00002', 'Geography', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00003', 'Physics', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00004', 'Chemistry', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00005', 'Biology', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00006', 'Additional Mathematics', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00007', 'Pure Mathematics', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00008', 'Statistics', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00009', 'Literature in English', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00010', 'Literature in Zimbabwe Indigenous Languages', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00011', 'History', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00012', 'Sociology', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00013', 'Economic History', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00014', 'Family and Religious Studies', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00015', 'Business & Enterprise Skills', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00016', 'Commerce', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00017', 'Commercial Studies', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00018', 'Economics', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00019', 'Principles of Accounts', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00020', 'Technical Vocational', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00021', 'Building Technology and Design', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00022', 'Design and Technology', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00023', 'Food Technology and Design', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00024', 'Metal Technology and Design', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00025', 'Home Management and Design', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00026', 'Technical Graphics and Design', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00027', 'Textile Technology and Design', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00028', 'Wood Technology and Design', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00029', 'Art', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00030', 'Dance', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00031', 'Musical Arts', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SUBID00032', 'Theatre Arts', 'O level','Zimsec','AM2663','2023-01-04 13:58:58','2023-01-04 13:58:58','Null');