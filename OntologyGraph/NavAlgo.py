from OntologyGraph import Database as DB
#import ObjectDetection.yolo8_custom_live as obj1
obj=["Sofa","table","chair"]
queryFront="SELECT Infront FROM map ;"
queryLeft="SELECT Leftside FROM map ;"
queryFarLeft="SELECT FarLeft FROM map ;"
queryRight="SELECT Rightside FROM map ;"
queryFarRight="SELECT FarRight FROM map ;"
queryBehind="SELECT Behind FROM map ;"
queryCenter="SELECT Center FROM map ;"
queryWindowBehind="SELECT Window_behind FROM map ;"
queryWindowFront="SELECT Window_front FROM map ;"
queryWindowLeft="SELECT Window_left FROM map ;"
queryWindowRight="SELECT Window_right FROM map ;"

DB.mycursor.execute(queryFront)
record=DB.mycursor.fetchall()
front=record[0][0]

DB.mycursor.execute(queryLeft)
record=DB.mycursor.fetchall()
Left=record[0][0]

DB.mycursor.execute(queryFarLeft)
record=DB.mycursor.fetchall()
FarLeft=record[0][0]

DB.mycursor.execute(queryRight)
record=DB.mycursor.fetchall()
Right=record[0][0]

DB.mycursor.execute(queryFarRight)
record=DB.mycursor.fetchall()
FarRight=record[0][0]

DB.mycursor.execute(queryBehind)
record=DB.mycursor.fetchall()
Behind=record[0][0]

DB.mycursor.execute(queryCenter)
record=DB.mycursor.fetchall()
Center=record[0][0]

DB.mycursor.execute(queryWindowBehind)
record=DB.mycursor.fetchall()
Windowbehind=record[0][0]

DB.mycursor.execute(queryWindowFront)
record=DB.mycursor.fetchall()
WindowFront=record[0][0]

DB.mycursor.execute(queryWindowRight)
record=DB.mycursor.fetchall()
WindowRight=record[0][0]

DB.mycursor.execute(queryWindowLeft)
record=DB.mycursor.fetchall()
WindowLeft=record[0][0]
"""
start=True
detected_list=0
previous_objects=[]
while start:
    for i in range(len(obj)):
        while i==5:
            if obj[i]==Left:
                previous_objects.append(obj)
                i+=1
            if obj[i]==front or obj[i]==Center:
                previous_objects.append(obj)
                i+=1
            if obj[i]==Right:
                previous_objects.append(obj)
                i += 1
        if ((Left == "" or Center == "" or Right == "") and (len(previous_objects)>=2)) or (previous_objects==3):
            print("You are near the door.")
        else:
            pass
"""





