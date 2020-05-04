-- MySQL Script generated by MySQL Workbench

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';


-- -----------------------------------------------------
-- Schema Library
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Library` DEFAULT CHARACTER SET latin1 ;
USE `Library` ;

-- -----------------------------------------------------
-- Table `Library`.`Roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Roles` (
  `RoleID` INT(11) NOT NULL AUTO_INCREMENT,
  `Title` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`RoleID`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `Library`.`Persons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Persons` (
  `PersonID` INT(11) NOT NULL AUTO_INCREMENT,
  `LastName` VARCHAR(255) NULL DEFAULT NULL,
  `FirstName` VARCHAR(255) NULL DEFAULT NULL,
  `City` VARCHAR(255) NULL DEFAULT NULL,
  `Address` VARCHAR(255) NULL DEFAULT NULL,
  `PostalCode` VARCHAR(255) NULL DEFAULT NULL,
  `PhoneNumber` VARCHAR(255) NULL DEFAULT NULL,
  `Email` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`PersonID`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `Library`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Users` (
  `UserID` INT(11) NOT NULL AUTO_INCREMENT,
  `Username` VARCHAR(255) NULL DEFAULT NULL,
  `Password` VARCHAR(255) NULL DEFAULT NULL,
  `RoleID` INT(11) NOT NULL,
  `PersonID` INT(11) NOT NULL,
  PRIMARY KEY (`UserID`, `RoleID`, `PersonID`),
  INDEX `fk_User_Role_idx` (`RoleID` ASC),
  INDEX `fk_Users_Persons1_idx` (`PersonID` ASC),
  CONSTRAINT `fk_User_Role`
    FOREIGN KEY (`RoleID`)
    REFERENCES `Library`.`Roles` (`RoleID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_Persons1`
    FOREIGN KEY (`PersonID`)
    REFERENCES `Library`.`Persons` (`PersonID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `Library`.`Books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Library`.`Books` (
  `BookID` INT(11) NOT NULL AUTO_INCREMENT,
  `Title` VARCHAR(255) NULL DEFAULT NULL,
  `Author` VARCHAR(255) NULL DEFAULT NULL,
  `Year` VARCHAR(255) NULL DEFAULT NULL,
  `UserID` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`BookID`),
  INDEX `fk_Book_User1_idx` (`UserID` ASC),
  CONSTRAINT `fk_Book_User1`
    FOREIGN KEY (`UserID`)
    REFERENCES `Library`.`Users` (`UserID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
