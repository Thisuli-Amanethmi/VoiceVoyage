package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class activityObjectDetectionAndNavigation extends AppCompatActivity {
    Button button_back;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_object_detection_and_navigation_screen);

        // Initialize buttons
        button_back = findViewById(R.id.button_back);

        // Handle button click
        button_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityObjectDetectionAndNavigation.this, activityUserHome.class);

                // Start the next activity
                startActivity(intent);
            }
        });
    }
}
