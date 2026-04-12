import mysql.connector
con = mysql.connecter.connect(
	host="localhost",
	user="root",
	password="root",
	database="niis"
)
if con:
	print("connected")
else:
	print("not connected")
	