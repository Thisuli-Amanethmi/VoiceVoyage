package com.example.voicevoyageapplication;

import android.os.Bundle;
import android.view.Menu;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class activityHomeScreen extends AppCompatActivity {
//    @Override
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_home_screen);
//
//        // Retrieve data passed from the previous activity
//        String userName = getIntent().getStringExtra("USER_NAME");
//        String emailAddress = getIntent().getStringExtra("EMAIL_ADDRESS");
//        String password = getIntent().getStringExtra("PASSWORD");
//
//        // Do whatever you need with the retrieved data
//    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home_screen);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.activity_home_menu_main, menu);
        return true;
    }

//    @Override
//    public boolean onOptionsItemSelected(MenuItem item) {
//        // Handle item selection
//        switch (item.getItemId()) {
//            case R.id.action_start_navigation:
//                showToast("Start Navigation");
//                return true;
//            case R.id.action_enter_house_layout:
//                showToast("Enter House Layout");
//                return true;
//            case R.id.action_settings:
//                showToast("Settings");
//                return true;
//            default:
//                return super.onOptionsItemSelected(item);
//        }
//    }

    private void showToast(String message) {
        Toast.makeText(this, message, Toast.LENGTH_SHORT).show();
    }
}
