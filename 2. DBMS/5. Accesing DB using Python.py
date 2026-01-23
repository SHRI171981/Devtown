import sqlite3 as sq #sql library
database = sq.connect('test.db') #extension is db
print('Database successfully created')
print(database)

#database.execute function -> executing sql query
database.execute('''
create table new(
            Name char(100),
            Age int);
'''
)
print("table created")
database.execute("insert into new values('Tony',45);")

data=database.execute('Select * from new')
for i in data:
    print(i)

# THIS CAN BE USED ONLY IN COLAB

