import mysql.connector
import RoomFormat as RF

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ontology"
)

mycursor = mydb.cursor()

sql_insertion1 = "INSERT INTO map(Infront, Leftside, FarLeft, Rightside, FarRight, Behind, Center) VALUES (%s,%s,%s,%s,%s,%s,%s)"
val = (RF.in_front,RF.to_the_left,RF.far_left,RF.to_the_right,RF.far_right,RF.behind_you,RF.center)
mycursor.execute(sql_insertion1, val)

last_id = mycursor.lastrowid

if RF.window_on_left_wall.lower() == "yes":
  sql_update = "UPDATE map SET Window_left = %s WHERE ID = %s"
  mycursor.execute(sql_update, (1, last_id))
if RF.window_on_right_wall.lower() == "yes":
  sql_update = "UPDATE map SET Window_right = %s WHERE ID = %s"
  mycursor.execute(sql_update, (1, last_id))
if RF.window_near_door.lower() == "yes":
  sql_update = "UPDATE map SET Window_behind = %s WHERE ID = %s"
  mycursor.execute(sql_update, (1, last_id))
if RF.window_on_front_wall.lower() == "yes":
  sql_update = "UPDATE map SET Window_front = %s WHERE ID = %s"
  mycursor.execute(sql_update, (1, last_id))

mydb.commit()