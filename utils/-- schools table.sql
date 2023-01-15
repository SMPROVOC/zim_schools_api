-- schools table

INSERT INTO schools ( scid, name, province, motto, denomination, founded, authority, gender, average_class_size, classes_offered, languages, colors, slogan, sports, nickname, coordinates, address, badge, is_boarding, created_at, updated_at, deleted_at)
 VALUES 
('SC00001','Allan Wilson','Harare province','We are Men of Men','non-denominated','1940','Government / Public School','Boys only','47 pupils','Form 1 to Upper 6','English & Shona','Black, Red and White','Sables the rare species','Rugby, Field Hockey, Football (Soccer)','DUB','17.77015°S 31.01076°E','N/A','N/A','Yes','2023-01-04 13:58:58','2023-01-04 13:58:58','Null'),
('SC00002','Arundel','Harare province','Gratia Et Scientia','Interdenominational','1955','Government / Public School','Girls only','40 pupils','Form 1 to Upper 6','English & Shona','N/A','N/A','N/A','N/A','17.7645277°S 31.0406769°E','N/A','N/A','Yes','2023-01-04 13:58:58','2023-01-04 13:58:58','Null')
('SC00003','Eaglesvale Senior','Harare province','Diens','Interdenominational','1911','Government / Public School','Girls only','25 pupils','Form 1 to Upper 6','English & Shona','N/A','N/A','N/A','VALE','17.7645277°S 31.0406769°E','N/A','N/A','Yes','2023-01-04 13:58:58','2023-01-04 13:58:58','Null');



CREATE TABLE Schools (
    ID INT IDENTITY(1,1) NOT NULL UNIQUE,
    SCID varchar(255) NOT NULL UNIQUE,
    Name varchar(255) NOT NULL,
    Province varchar(255) NOT NULL, 
    Motto varchar(255) NOT NULL,
    Denomination varchar(255) NOT NULL,
    Founded varchar(255) NOT NULL,
    Authority varchar(255) NOT NULL,
    Gender varchar(255) NOT NULL,
    Average_class_size varchar(255) NOT NULL,
    Classes_offered varchar(255) NOT NULL,
    Languages varchar(255) NOT NULL,
    Colors varchar(255) NOT NULL,
    Slogan varchar(255) NOT NULL,
    Sports varchar(255) NOT NULL,
    Nickname varchar(255) NOT NULL,
    Coordinates varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    Badge varchar(255) NOT NULL,
    Is_boarding varchar(255) NOT NULL,
    Created_at varchar(255) NOT NULL,
    Updated_at varchar(255) NOT NULL,
    Deleted_at varchar(255) NOT NULL

);