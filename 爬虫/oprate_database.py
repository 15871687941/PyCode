import sqlite3 as sq3
connection = sq3.connect("blindDate.db")
cursion = connection.cursor()
sql_create = '''create table girl(
id varchar(20) primary key,
userid varchar(20),
username varchar(50),
gender varchar(20),
birthday varchar(20),
height varchar(20),
province varchar(20),
city varchar(20),
education varchar(20),
monolog varchar(200),
image varchar(200)
)'''
sql_insert = '''
insert into table( , , , , ,) values(?, ?, ?, ?, ?)
'''
sql_delete = '''
drop table girl
'''
sql_select = '''
select * from girl
'''
cursion.execute(sql_select)
all = cursion.fetchall()
print(all)
cursion.close()
connection.commit()
connection.close()