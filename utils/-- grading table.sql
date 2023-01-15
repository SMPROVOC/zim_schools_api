-- grade table

CREATE TABLE Grades (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    GID varchar(255) NOT NULL UNIQUE,
    UID varchar(255) NOT NULL,
    SID varchar(255) NOT NULL,
    SCID varchar(255) NOT NULL, 
    Marks_By_Subject varchar(255) NOT NULL,
    Term varchar(255) NOT NULL, 
    Level varchar(255) NOT NULL, 
    Percentage varchar(255) NOT NULL, 
    Grading_structure varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);

INSERT INTO Grades ( GID, UID, SID, SCID, Marks_By_Subject, Term, Level, Percentage, Grading_structure, created_at, updated_at, deleted_at)
 VALUES 
('GID00001', 'UID0001', 'SID00001','SCID00001','{"SUBID00001":{"Grade": "A", "Mark":86}, "SUBID00002":{"Grade": "B", "Mark":70}}', 'Term 1', 'O level', '67%', 'GS00001','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('GID00002', 'UID0001', 'SID00001','SCID00001','{"SUBID00001":{"Grade": "B", "Mark":76}, "SUBID00002":{"Grade": "C", "Mark":50}}', 'Final Zimsec', 'A level', '47%', 'GS00001','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('GID00003', 'UID0001', 'SID00001','SCID00001','{"SUBID00001":{"Grade": "A", "Mark":86}, "SUBID00002":{"Grade": "D", "Mark":40}}', 'Term 3', 'O level', '87%', 'GS00001','2023-01-04 13:58:58','2023-01-04 13:58:58','Null');

