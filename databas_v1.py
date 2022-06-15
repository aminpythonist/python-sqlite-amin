

import sqlite3


# DB class
class Dadabase:

	# constructer
	def __init__(self):

		# create object sqlite3 connect file exist
		self.con = sqlite3.connect(r"C:\Users\DELL\Desktop\Pyhon Biggener Toturial\6\test.db")

		# creatre cursor for execute process
		self.cur = con.cursor()

	# a method for create table
	def create_table():

		self.cur.execute('''CREATE TABLE user
	               (first_name VARCHAR(255) , last_name VARCHAR(255), password VARCHAR(255))''')
		self.con.commit()
		print('Table is created!')

	# a method for insert into table
	def insert():
		self.cur.execute("INSERT INTO user VALUES ('yasin','zeinliyan','123@adminfuckyouhacker@@')")
		self.con.commit()
		print('info is recorded!')

	# a method for delete into table
	def delete():

		self.cur.execute("DELETE FROM user WHERE first_name = 'yasin' ")
		self.con.commit()
		print('row is deleted!')


	# a method for update a row in table
	def update():

		self.cur.execute("UPDATE user SET first_name = 'amin' WHERE first_name = 'yasin'")
		self.con.commit()
		print('row is updated!')






























