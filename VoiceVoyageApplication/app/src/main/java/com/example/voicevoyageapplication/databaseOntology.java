package com.example.voicevoyageapplication;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class databaseOntology  extends SQLiteOpenHelper {
    public static final String DBName = "ontology.db"; // name of the database

    // constructor - creating database
    public databaseOntology(Context context) {
        super(context, "ontology.db", null, 1);
    }

    // create map table
    @Override
    public void onCreate(SQLiteDatabase MyDB) {
        MyDB.execSQL("create Table map(ID TEXT primary key, Infront TEXT, Leftside TEXT, FarLeft TEXT, " +
                "Rightside TEXT, FarRight TEXT, Behind TEXT, Center TEXT, " +
                "Window_left TEXT, Window_right TEXT, Window_behind TEXT, Window_front TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase MyDB, int i, int i1) {
        MyDB.execSQL("drop Table if exists map");
    }

    // insert data into the ontology table
    public Boolean insertDataMap(String ID, String inFront, String leftSide, String farLeft,
                                 String rightSide, String farRight, String behind, String center){
        // (,String windowLeft, String windowRight, String windowBehind, String windowFront)

        SQLiteDatabase MyDB = this.getWritableDatabase();

        ContentValues contentValues= new ContentValues();
        contentValues.put("ID", ID);
        contentValues.put("Infront", inFront);
        contentValues.put("Leftside", leftSide);
        contentValues.put("FarLeft", farLeft);
        contentValues.put("Rightside", rightSide);
        contentValues.put("FarRight", farRight);
        contentValues.put("Behind", behind);
        contentValues.put("Center", center);
//        contentValues.put("Window_left", windowLeft);
//        contentValues.put("Window_right", windowRight);
//        contentValues.put("Window_behind", windowBehind);
//        contentValues.put("Window_front", windowFront);

        long result = MyDB.insert("map", null, contentValues);

        if(result==-1) //insertion fails
            return false;
        else
            return true;
    }

    // left window
//    public Boolean insertLeftWindow(){
//        SQLiteDatabase MyDB = this.getWritableDatabase();
//
//        ContentValues values = new ContentValues();
//        values.put("Window_left", 1);
//
//        long result = MyDB.update("users", values, "Window_left", "1");
//
//        if(result==-1) //insertion fails
//            return false;
//        else
//            return true;
//    }

}
