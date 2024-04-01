package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class activityInstructions extends AppCompatActivity {
    Button button_back, button_agree;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_instructions_screen);

        // Initialize buttons
        button_agree = findViewById(R.id.agree_button);
        button_back = findViewById(R.id.back_button);

        // Handle button click
        button_agree.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityInstructions.this, activityHouseDescriptionOne.class);

                // Start the next activity
                startActivity(intent);
            }
        });

        button_back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityInstructions.this, activityUserHome.class);

                // Start the next activity
                startActivity(intent);
            }
        });
    }
}
