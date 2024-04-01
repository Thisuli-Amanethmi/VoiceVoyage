package com.example.voicevoyageapplication;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class databaseUserDetails extends SQLiteOpenHelper {
    public static final String DBName = "UserDetails.db"; // name of the database

    // constructor - creating database
    public databaseUserDetails(Context context) {
        super(context, "UserDetails.db", null, 1);
    }

    // create user table
    @Override
    public void onCreate(SQLiteDatabase MyDB) {
        MyDB.execSQL("create Table users(username TEXT primary key, email TEXT, password TEXT)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase MyDB, int i, int i1) {
        MyDB.execSQL("drop Table if exists users");
    }

    // insert data into the users table
    public Boolean insertData(String username, String email, String password){
        SQLiteDatabase MyDB = this.getWritableDatabase();

        ContentValues contentValues= new ContentValues();
        contentValues.put("username", username);
        contentValues.put("email", email);
        contentValues.put("password", password);

        long result = MyDB.insert("users", null, contentValues);

        if(result==-1) //insertion fails
            return false;
        else
            return true;
    }

    // to check username
    public Boolean checkUserName(String username) {
        SQLiteDatabase MyDB = this.getWritableDatabase();
        Cursor cursor = MyDB.rawQuery("Select * from users where username = ?", new String[]{username});

        if(cursor.getCount() > 0) // username exists
            return true;
        else
            return false;
    }

    // to check email
    public Boolean checkUserEmail(String email) {
        SQLiteDatabase MyDB = this.getWritableDatabase();
        Cursor cursor = MyDB.rawQuery("Select * from users where email = ?", new String[]{email});

        if(cursor.getCount() > 0) // email exists
            return true;
        else
            return false;
    }

    // to check user details
    public Boolean checkUser(String username, String email, String password){
        SQLiteDatabase MyDB = this.getWritableDatabase();
        Cursor cursor = MyDB.rawQuery("Select * from users where username = ? and email = ? and password = ?", new String[] {username, email, password});

        if(cursor.getCount()>0) // user exists
            return true;
        else
            return false;
    }

    // to check username & password
    public Boolean checkUserNamePassword(String username, String password){
        SQLiteDatabase MyDB = this.getWritableDatabase();
        Cursor cursor = MyDB.rawQuery("Select * from users where username = ? and password = ?", new String[] {username, password});

        if(cursor.getCount()>0) // user exists
            return true;
        else
            return false;
    }

}
