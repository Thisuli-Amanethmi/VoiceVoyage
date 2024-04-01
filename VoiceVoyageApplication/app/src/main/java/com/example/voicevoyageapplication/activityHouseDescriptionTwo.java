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

    // variables to store intent extras
    String userName, inFront, left, farLeft;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_house_description_two);

        // Retrieve the username from the intent extras
        Intent intent = getIntent();
        if(intent != null) {
            userName = getIntent().getStringExtra("USER_NAME");
            inFront = getIntent().getStringExtra("IN_FRONT_OBJECT");
            left = getIntent().getStringExtra("LEFT_OBJECT");
            farLeft = getIntent().getStringExtra("FAR_LEFT_OBJECT");
        }

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
                // Retrieve the data entered by the user
                String rightObject = rightEditText.getText().toString();
                String farRightObject = farRightEditText.getText().toString();
                String behindObject = behindEditText.getText().toString();
                String centerObject = centerEditText.getText().toString();

                // Pass the data to the next activity
                Intent intent = new Intent(activityHouseDescriptionTwo.this, activityHouseDescriptionThree.class);
                intent.putExtra("USER_NAME", userName);
                intent.putExtra("IN_FRONT_OBJECT", inFront);
                intent.putExtra("LEFT_OBJECT", left);
                intent.putExtra("FAR_LEFT_OBJECT", farLeft);
                intent.putExtra("RIGHT_OBJECT", rightObject);
                intent.putExtra("FAR_RIGHT_OBJECT", farRightObject);
                intent.putExtra("BEHIND_OBJECT", behindObject);
                intent.putExtra("CENTER_OBJECT", centerObject);

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
