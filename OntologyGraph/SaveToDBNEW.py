from OntologyGraph import Database as DB


def save_to_ontology_database(in_front, to_the_left, far_left, to_the_right, far_right, behind_you, center,
                      window_near_door, window_on_left_wall, window_on_right_wall, window_on_front_wall):
    val = (in_front, to_the_left, far_left, to_the_right, far_right, behind_you, center)
    sql_insertion1 = "INSERT INTO map(Infront, Leftside, FarLeft, Rightside, FarRight, Behind, Center) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    DB.mycursor.execute(sql_insertion1, val)

    last_id = DB.mycursor.lastrowid

    if window_on_left_wall.lower() == "yes":
        sql_update = "UPDATE map SET Window_left = %s WHERE ID = %s"
        DB.mycursor.execute(sql_update, (1, last_id))
    if window_on_right_wall.lower() == "yes":
        sql_update = "UPDATE map SET Window_right = %s WHERE ID = %s"
        DB.mycursor.execute(sql_update, (1, last_id))
    if window_near_door.lower() == "yes":
        sql_update = "UPDATE map SET Window_behind = %s WHERE ID = %s"
        DB.mycursor.execute(sql_update, (1, last_id))
    if window_on_front_wall.lower() == "yes":
        sql_update = "UPDATE map SET Window_front = %s WHERE ID = %s"
        DB.mycursor.execute(sql_update, (1, last_id))

    DB.mydb.commit()

