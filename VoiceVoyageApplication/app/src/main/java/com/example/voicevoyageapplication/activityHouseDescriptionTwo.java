package com.example.voicevoyageapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;

public class activityHouseDescriptionTwo extends AppCompatActivity {
    Button nextButton, previousButton;
    EditText rightEditText, farRightEditText, behindEditText, centerEditText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_house_description_two);

        // Initialize views
        rightEditText = findViewById(R.id.rightEditText);
        farRightEditText = findViewById(R.id.farRightEditText);
        behindEditText = findViewById(R.id.behindEditText);
        centerEditText = findViewById(R.id.centerEditText);
        previousButton = findViewById(R.id.previous_button);
        nextButton = findViewById(R.id.next_button);

        // Handle button click
        nextButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityHouseDescriptionTwo.this, activityHouseDescriptionThree.class);

                // Start the next activity
                startActivity(intent);
            }
        });

        previousButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Pass the data to the next activity
                Intent intent = new Intent(activityHouseDescriptionTwo.this, activityHouseDescriptionOne.class);

                // Start the next activity
                startActivity(intent);
            }
        });
    }

}
