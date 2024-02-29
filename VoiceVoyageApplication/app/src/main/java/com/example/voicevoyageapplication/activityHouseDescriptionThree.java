package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class activityHouseDescriptionThree extends AppCompatActivity {
    Button previousButton, submitButton;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_house_description_three);

        // Initialize views
        previousButton = findViewById(R.id.previous_button);
        submitButton = findViewById(R.id.submit_button);

        // Handle submit button click
        previousButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityHouseDescriptionThree.this, activityHouseDescriptionTwo.class);

                // Start the next activity
                startActivity(intent);
            }
        });

        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                // Intent intent = new Intent(activityHouseDescriptionThree.this, activityHouseLayout.class);

                // Start the next activity
                // startActivity(intent);
            }
        });
    }
}
