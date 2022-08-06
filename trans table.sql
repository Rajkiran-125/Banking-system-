use bank;
create table trans(
	acc_no int,
    amt int,
    type char(10),
    date datetime default now()
);
desc trans;
insert into trans (acc_no,amt,type) values(123,5654,'deposit');
select * from trans;