-- ---------------------------------------------------------------
-- MySQL script that initializes database 'Library' using the 
-- necessary SQL commands.
-- ---------------------------------------------------------------


USE Library;


-- Inserting the roles that a user can have.

INSERT INTO Roles (Title) VALUES ("Visitor");
INSERT INTO Roles (Title) VALUES ("Editor");
INSERT INTO Roles (Title) VALUES ("Admin");


-- Inserting an admin.

INSERT INTO Persons (LastName,FirstName) VALUES ("Test","test");

INSERT INTO Users (Username,Password,RoleID,PersonID) VALUES ("Test","123456789",3,1);
