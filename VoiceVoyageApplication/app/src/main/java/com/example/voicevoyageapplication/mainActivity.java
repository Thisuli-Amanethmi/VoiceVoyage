package com.example.voicevoyageapplication;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;

import androidx.appcompat.app.AppCompatActivity;

public class mainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        activityFirstScreen aa = new activityFirstScreen();
        activityUserHome bb = new activityUserHome();

        // Check if it's the first launch
        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);
        boolean isFirstLaunch = prefs.getBoolean("isFirstLaunch", true);

        // If it's the first launch, show first screen
        if (isFirstLaunch) {
            setContentView(R.layout.activity_first_screen);
            aa.onCreate(savedInstanceState);

            // Update the flag to indicate that the app has been launched before
            prefs.edit().putBoolean("isFirstLaunch", false).apply();
        } else {
            // If it's not the first launch, show user home screen
            setContentView(R.layout.activity_user_home_screen);
            bb.onCreate(savedInstanceState);
        }
    }
}
