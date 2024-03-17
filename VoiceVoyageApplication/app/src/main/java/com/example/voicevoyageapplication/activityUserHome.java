package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class activityUserHome extends AppCompatActivity {

    Button button_instruction, button_navigation, button_settings;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_user_home_screen);

        // Initialize buttons
        button_instruction = findViewById(R.id.button_instructions);
        button_navigation = findViewById(R.id.button_navigation);
        button_settings = findViewById(R.id.button_settings);

        // Handle button click
        button_instruction.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityUserHome.this, activityInstructions.class);

                // Start the next activity
                startActivity(intent);
            }
        });

        button_navigation.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityUserHome.this, activityNavigation.class);

                // Start the next activity
                startActivity(intent);
            }
        });

        button_settings.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityUserHome.this, activitySettings.class);

                // Start the next activity
                startActivity(intent);
            }
        });

    }

}
