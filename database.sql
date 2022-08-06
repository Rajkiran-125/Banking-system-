create database bank;
use bank;
create table accounts (
	acc_no int primary key,
    name char(20),
    dob char(20),
    address char(20),
    contact int,
    balance int
    );
desc accounts;
    